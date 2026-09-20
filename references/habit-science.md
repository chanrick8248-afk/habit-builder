# Habit Science Background

Reference notes for the Habit Builder skill. Load this only when the user pushes back on the method ("does this actually work?", "what's the evidence?", "why bother with cues?") or asks for a deeper rationale than the simple steps in SKILL.md. Do not surface this in default conversations - it is background, not pitch material.

The summary below gives enough to answer an "is there evidence?" question without sending the user down a citation rabbit hole.

## The habit loop: cue -> craving -> response -> reward

Duhigg (2012) popularized the four-step habit loop and explicitly modeled it on the work of behaviorists like Skinner and the cognitive research coming out of MIT's Ann Graybiel lab. The current consensus view in neuroscience is:

- **Basal ganglia** holds the habit chunk once it is automatic.
- **Cue + reward** stays in working memory long after the routine becomes unconscious.
- A "want" (craving) is what bridges cue to response - this is what distinguishes a habit from a pure stimulus-response reflex.

Implication for the skill: a routine without a clear craving almost always dies, even if the cue is reliable. When a user's plan keeps stalling, the missing piece is almost always the craving/reward connection, not the cue.

## Implementation intentions (Gollwitzer)

Gollwitzer's "implementation intention" studies (1993, 1999 meta-analyses) consistently show that writing a specific "if-then" plan roughly doubles follow-through versus a generic goal. The IF-THEN format is exactly the skill's "I will BEHAVIOR at TIME in LOCATION" sentence.

Mechanism: it offloads the decision from deliberative cognition at the moment of action. The cue is decided in advance; the user does not need motivation at execution time.

## Habit stacking (BJ Fogg)

Fogg's "Tiny Habits" method (2019) formalized habit stacking as a learnable behavior-design pattern. The empirical claim - that attaching a new behavior to an existing high-reliability behavior inherits the reliability - has not been rigorously tested in randomized trials, but the underlying principle (leveraging existing cues with high discriminability) is well-supported by associative learning research.

Practical guard-rail: only stack onto a behavior that already happens at >90% reliability. "After I check my email" is a bad anchor because checking email is itself variable; "after I brush my teeth at night" is a good anchor because it has the same time and place every day.

## Never-miss-twice rule

This comes from performance coaching literature, not from a peer-reviewed source. The intuition is straight relapse prevention: a single missed instance is noise; two consecutive misses is a statistically meaningful signal that the behavior is no longer on autopilot. Resuming after one miss is routine; resuming after two is recovery.

Use the rule as a self-monitoring heuristic, not as a moral rule. Missing two does not mean the user has "failed" - it means the loop has been disrupted and needs a diagnostic (cue too weak? routine too big? reward gone?).

## Time to automaticity: the 21 / 66 / 254 myth

Lally et al. (2010, European Journal of Social Psychology) found the median time to automaticity for a new behavior was 66 days, with a range of 18 to 254, depending on the behavior's complexity. The popular "21 days" claim traces to Maxwell Malt's psycho-cybernetics, not to data.

Skill implication: tell users that the 4-8 week range in SKILL.md is a working estimate, not a deadline. Some behaviors (drinking a glass of water) hit automaticity in weeks; others (regular exercise) can take half a year.

## Identity-based habits (James Clear)

Clear (2018) re-popularized the identity framing: lasting change happens when the user starts acting "as the type of person who does X". This is a useful narrative frame but is not a separately tested intervention; the underlying effect is probably the same as implementation intentions - shifting self-categorization reduces the cognitive load of each individual decision.

Resist treating identity statements as a magic ingredient. They work best as reinforcement for behavior, not as a substitute for designing a workable cue and routine.

## What the science does NOT support

- "Motivation is the fuel." No - motivation is highly context-dependent and decays. The skill is built around this: design so that execution does not require motivation.
- "Discipline is the bottleneck." Also no - environments beat willpower (Wansink, 2010 on kitchen placement, though many specific claims have replication issues).
- "Cold-turkey quitting works for all habits." No - nicotine research (Stitzer & Gross, 1988) shows gradual reduction with substitution outperforms abrupt cessation for many people. For bad-habit removal, the skill's "remove cue + add friction" is closer to the gradual-with-substitution approach.

## Quick "is there evidence?" answers

| User asks | Source |
|-----------|--------|
| "Does writing it down help?" | Gollwitzer 1999 meta-analysis |
| "Will it really take 2 months?" | Lally 2010 study (66-day median) |
| "Should I just use willpower?" | Baumeister ego-depletion debate - evidence is weak; environment design wins |
| "What about motivation?" | Self-determination theory (Deci & Ryan) - motivation is a follower of context, not a leader |
| "Why bother with stacking?" | Skinnerian reinforcement + BJ Fogg Tiny Habits |
| "Why even bother with habits at all?" | Wood & Neal 2007 - health behaviors are mostly habitual, not deliberative |
