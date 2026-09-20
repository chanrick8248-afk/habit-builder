# habit-builder

A WorkBuddy / Claude skill that turns a vague intention ("exercise more") into a one-page, trackable habit system.

## What it does

Eight-step framework — define the smallest behavior, map the cue-craving-routine-reward loop, write an implementation intention, stack onto an existing anchor, design the environment, track with a never-miss-twice rule, review weekly, then scale.

Based on Gollwitzer (implementation intentions), Fogg (Tiny Habits), Lally et al. (66-day median to automaticity) and Clear (identity-based habits).

## Files in this skill

```
.
├── SKILL.md                              # The main entry point. LLM reads this.
├── references/
│   └── habit-science.md                  # Background evidence, loaded on demand.
├── assets/
│   └── one-page-plan-template.md         # The one-page plan output template.
├── scripts/
│   └── check_habit_plan.py               # Validator: verifies the filled plan has every section.
└── README.md                             # You are here.
```

## How an LLM uses it

When a user says things like "help me build a habit", "I want to exercise more but can't stick with it", "why do my habits keep failing", load the skill and follow `SKILL.md` step 1 → 8. Fill in `assets/one-page-plan-template.md` and hand back the completed plan. Optionally validate with `scripts/check_habit_plan.py`. Reach for `references/habit-science.md` only if the user asks "is there evidence?" or pushes back on the method.

## Disclaimer

General self-improvement education, not professional medical or psychological advice. Consult a qualified professional for clinical concerns.

## License

Released for personal use. Upstream: `SkillMedev/skills` on GitHub.
