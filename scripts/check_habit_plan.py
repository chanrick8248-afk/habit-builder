#!/usr/bin/env python3
"""
check_habit_plan.py

Verify a filled-in one-page habit plan (based on assets/one-page-plan-template.md)
covers every required section. Run after the user fills in the template:

    python3 scripts/check_habit_plan.py path/to/filled-plan.md

The script:
  - reads the markdown file
  - for each section in the canonical template, reports FILLED / PLACEHOLDER / MISSING
  - flags routine lines that are oversized (more than ~30 words = probably too big)
  - prints a short summary; exits non-zero if any required section is incomplete

It is deterministic on purpose - the same plan always gets the same report, so the
LLM does not have to re-read the file just to validate it.

Why this exists: SKILL.md step 6 calls out tracking without perfectionism, but it is
easy for a filled plan to quietly still contain [BRACKETS] or the two-minute version
to balloon into a full workout. This script catches both.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Canonical sections, in order, matching assets/one-page-plan-template.md.
SECTIONS = [
    "Identity statement",
    "Implementation intention",
    "Habit loop mapping",
    "Environment design",
    "Two-minute version",
    "Tracking method",
    "Weekly review",
    "Scaling plan",
]

# Recognized placeholder patterns. If a section still contains any of these,
# it counts as PLACEHOLDER, not FILLED.
PLACEHOLDER_RE = re.compile(r"\[[^\]]*\]|\bTODO\b|\bTBD\b|\bxxx\b", re.IGNORECASE)

# Headings that mark each section.
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

# A "routine" is the action line in section 3. We flag if it is unusually long,
# because Step 1 of SKILL.md specifically says keep the routine small.
ROUTINE_TOO_LONG_WORDS = 30

# A "long paragraph" inside any section - the template's footer explicitly says
# "if a section is forcing you to write more than a sentence, shrink the section".
LONG_PARAGRAPH_CHARS = 220


def _section_key(heading: str) -> str | None:
    """Match canonical SECTIONS even when a heading has a numeric prefix like
    '1. Identity statement' or trailing punctuation."""
    for canonical in SECTIONS:
        if canonical in heading:
            return canonical
    return None


def read_sections(text: str) -> dict[str, str]:
    """Return a dict of {section_name: content} from the markdown body."""
    lines = text.splitlines()
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            key = _section_key(m.group(2).strip())
            if key is not None:
                current = key
                sections[current] = []
                continue
        if current is not None:
            sections[current].append(line)
    return {name: "\n".join(body).strip() for name, body in sections.items()}


def classify(content: str) -> str:
    """Decide if a section is FILLED, PLACEHOLDER, or EMPTY."""
    if not content:
        return "MISSING"
    if PLACEHOLDER_RE.search(content):
        return "PLACEHOLDER"
    if len(content.strip()) < 5:
        return "PLACEHOLDER"
    return "FILLED"


def warn_oversized(name: str, content: str) -> list[str]:
    """Return human-readable warnings for sections that look too long."""
    warnings: list[str] = []
    if not content:
        return warnings

    # Long uninterrupted paragraph
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", content) if p.strip()]
    for i, para in enumerate(paragraphs, 1):
        if len(para) > LONG_PARAGRAPH_CHARS:
            warnings.append(
                f"{name}: paragraph {i} is {len(para)} chars - "
                "the template says one section = one sentence; consider shrinking."
            )

    # Routine specifically
    if name == "Habit loop mapping":
        # Pull the row whose left column starts with "Routine"
        for line in content.splitlines():
            if re.match(r"\|\s*Routine", line, re.IGNORECASE):
                # Drop the leading "Routine" cell, then take everything after
                parts = [p.strip() for p in line.split("|")[1:]]
                routine_text = " ".join(p for p in parts if p).strip()
                word_count = len(routine_text.split())
                if word_count > ROUTINE_TOO_LONG_WORDS:
                    warnings.append(
                        f"Routine line has {word_count} words - "
                        "Step 1 of SKILL.md says keep the routine small. "
                        "Shrink until the worst-day version still fits."
                    )
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", help="Path to the filled-in one-page plan")
    args = parser.parse_args()

    path = Path(args.plan)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    sections = read_sections(text)

    statuses: dict[str, str] = {}
    failures = 0
    print(f"Checking plan: {path}")
    print("-" * 60)

    for section in SECTIONS:
        body = sections.get(section, "")
        status = classify(body)
        statuses[section] = status
        marker = {
            "FILLED": "[OK]   ",
            "PLACEHOLDER": "[TODO] ",
            "MISSING": "[MISS] ",
        }[status]
        print(f"{marker}{section}")
        if status != "FILLED":
            failures += 1
        for w in warn_oversized(section, body):
            print(f"        ! {w}")

    print("-" * 60)
    total = len(SECTIONS)
    filled = sum(1 for s in statuses.values() if s == "FILLED")
    print(f"Summary: {filled}/{total} sections fully filled.")

    if failures == 0:
        print("Plan looks complete. Run the weekly review on Sunday evening.")
        return 0
    print(
        f"{failures} section(s) need attention - fill in the bracketed "
        "placeholders or expand the section, then re-run."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
