"""Check the published instruction package using only the standard library.

This checks packaging, not the behavior of a language model.
"""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path("skills/relay-ledger/SKILL.md")
MAX_ENTRY_BYTES = 6000
MAX_ENTRY_WORDS = 700


def check(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    required = [SKILL, Path("LICENSE"), Path("README.md"), Path("README.zh-CN.md")]
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"Missing {relative}")
    if not (root / SKILL).is_file():
        return errors
    entry = (root / SKILL).read_text(encoding="utf-8")
    parts = entry.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        errors.append("SKILL.md needs frontmatter")
    else:
        fields = dict(re.findall(r"^([a-z-]+):\s*(.+)$", parts[1], re.MULTILINE))
        if fields.get("name") != "relay-ledger":
            errors.append("Skill name must match its directory")
        if not fields.get("description") or len(fields["description"]) > 1024:
            errors.append("Description must contain 1..1024 characters")
    if len(entry.encode("utf-8")) > MAX_ENTRY_BYTES or len(entry.split()) > MAX_ENTRY_WORDS:
        errors.append("Entrypoint exceeds the documented package context ceiling")

    versions = []
    for host in ("claude", "codex"):
        manifest_path = root / f".{host}-plugin/plugin.json"
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if manifest.get("name") != "relay-ledger":
                errors.append(f"{host} manifest has a different plugin identity")
            version = manifest.get("version", "")
            if not re.fullmatch(r"\d+\.\d+\.\d+", version):
                errors.append(f"{host} manifest needs a release version")
            versions.append(version)
            if host == "codex" and manifest.get("skills") != "./skills/":
                errors.append("Codex must load the canonical skills directory")
            if host == "claude" and "skills" in manifest:
                errors.append("Claude must use default canonical skills discovery")
            if any(key in manifest for key in ("hooks", "mcpServers", "apps", "agents", "commands")):
                errors.append(f"Unexpected runtime component in {host} manifest")
        except (OSError, ValueError, AttributeError, TypeError) as error:
            errors.append(f"Invalid {host} manifest: {error}")
    if len(set(versions)) > 1:
        errors.append("Host manifest versions disagree")
    try:
        suite = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))
        cases = suite["cases"]
        ids = [case["id"] for case in cases]
        if len(ids) != len(set(ids)):
            errors.append("Duplicate evaluation case ID")
        if not cases or any(not case.get("prompt") or not case.get("expected") for case in cases):
            errors.append("Evaluation cases need prompts and observable expectations")
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors.append(f"Invalid evaluation cases: {error}")

    for file in root.rglob("*"):
        relative = file.relative_to(root)
        if any(part in {".git", "__pycache__", "dist"} for part in relative.parts):
            continue
        if file.is_symlink():
            errors.append(f"Symlink not allowed in release source: {relative}")
            continue
        if not file.is_file() or file.suffix not in {".md", ".yaml", ".yml"}:
            continue
        content = file.read_text(encoding="utf-8")
        if re.search(r"(?<![A-Za-z])[A-Za-z]:[\\/]|/home/[^/\s]+/|/Users/[^/\s]+/", content):
            errors.append(f"Machine-specific path in {relative}")
        if file.suffix != ".md":
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            destination = (file.parent / target.split("#", 1)[0]).resolve()
            if not destination.is_relative_to(root):
                errors.append(f"Link escapes package: {relative}: {target}")
            elif not destination.exists():
                errors.append(f"Broken link: {relative}: {target}")
    return errors


if __name__ == "__main__":
    failures = check(ROOT)
    if failures:
        print("\n".join(failures))
        sys.exit(1)
    entry = (ROOT / SKILL).read_text(encoding="utf-8")
    print(f"Package valid; entrypoint {len(entry.split())} words / {len(entry.encode('utf-8'))} UTF-8 bytes.")
