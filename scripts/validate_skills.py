#!/usr/bin/env python3
"""Validate the Intelligems skill catalog."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

SECRET_PATTERNS = {
    "github token": re.compile(r"gh[oprsu]_[A-Za-z0-9_]{20,}"),
    "stripe live key": re.compile(r"sk_live_[A-Za-z0-9]{16,}"),
    "stripe restricted key": re.compile(r"rk_live_[A-Za-z0-9]{16,}"),
    "aws access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "slack token": re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    "google api key": re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
    "shopify token": re.compile(r"shpat_[A-Za-z0-9]{20,}"),
    "jwt": re.compile(r"eyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{10,}"),
    "presigned url signature": re.compile(r"(X-Amz-Signature=|AWSAccessKeyId=)[A-Za-z0-9%_-]+"),
    "private key": re.compile(r"BEGIN (RSA|OPENSSH|EC|DSA)? ?PRIVATE KEY"),
    "literal api key header": re.compile(
        r"intelligems-access-token:\s*(?!\$|<|YOUR_|your-api-key)[A-Za-z0-9][A-Za-z0-9_.-]{12,}",
        re.IGNORECASE,
    ),
    "shopify store domain": re.compile(r"\b(?!example-store)[A-Za-z0-9-]+\.myshopify\.com\b"),
}

FORBIDDEN_PUBLIC_PHRASES = (
    "Victor",
    "Victorpay",
    "Second Brain",
    "CleanShot",
    "personal account",
    "personal repo",
    "restored repo",
    "restored under",
    "dirty worktree",
    "internal demo",
    "Slack content",
    "private Slack",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} must start with YAML frontmatter")
    try:
        _, frontmatter, body = text.split("---\n", 2)
    except ValueError:
        fail(f"{path.relative_to(ROOT)} has malformed YAML frontmatter")
    if not body.strip():
        fail(f"{path.relative_to(ROOT)} has no body")

    data: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)} has invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def validate_skill(path: Path) -> None:
    data = parse_frontmatter(path)
    for required in ("name", "description", "license"):
        if not data.get(required):
            fail(f"{path.relative_to(ROOT)} missing frontmatter field: {required}")
    if data["name"] != path.parent.name:
        fail(
            f"{path.relative_to(ROOT)} name must match parent directory "
            f"({path.parent.name}), got {data['name']}"
        )
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", data["name"]):
        fail(f"{path.relative_to(ROOT)} has non-portable skill name: {data['name']}")
    if "--" in data["name"] or data["name"].endswith("-"):
        fail(f"{path.relative_to(ROOT)} has non-portable skill name: {data['name']}")
    if len(data["description"]) < 40:
        fail(f"{path.relative_to(ROOT)} description is too short")
    if len(data["description"]) > 1024:
        fail(f"{path.relative_to(ROOT)} description is too long")
    if data["license"] != "MIT":
        fail(f"{path.relative_to(ROOT)} license must be MIT")


def scan_secrets(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for label, pattern in SECRET_PATTERNS.items():
        match = pattern.search(text)
        if match:
            fail(f"{path.relative_to(ROOT)} may contain {label}: {match.group(0)[:40]}")
    if path == Path(__file__).resolve():
        return
    for phrase in FORBIDDEN_PUBLIC_PHRASES:
        if phrase in text:
            fail(f"{path.relative_to(ROOT)} contains internal-only phrase: {phrase}")


def main() -> int:
    if not SKILLS_DIR.exists():
        fail("missing skills directory")

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        fail("no skill SKILL.md files found")

    for skill in skill_files:
        validate_skill(skill)

    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            scan_secrets(path)

    print(f"Validated {len(skill_files)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
