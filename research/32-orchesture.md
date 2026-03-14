# Orchesture

**Repo:** https://github.com/yewon-yun/Orchesture
**Owner:** yewon-yun (1 follower)
**Stars:** 0
**Language:** Python
**Last Updated:** 2026-03-10

## What It Is

A gesture-controlled orchestra conducting system. Users conduct an orchestra in real time using both hands to control melody and harmony simultaneously — pitched as a more accessible alternative to traditional instruments.

**Two-hand role assignment:**
- **Right hand** → solo violin melody (main pitch)
- **Left hand** → orchestral accompaniment (chords)

**Pitch mapping:** Screen divided into 7 regions (C–B); wrist position determines pitch within region.

**Gesture modifiers (classified by KNN):**
| Gesture | Right Hand Effect | Left Hand Effect |
|---------|-------------------|-----------------|
| Fist | Stop note | Stop chord |
| OK sign | # (sharp) | 7th chord |
| Point (index up) | +1 octave | Minor chord |

**Custom gesture training:** Users capture webcam gestures labelled, then a KNN classifier is trained at runtime.

**Music output:** MIDI-style data → Logic Pro for orchestral sound generation

**Stack:** Python + MediaPipe + OpenCV + KNN (sklearn implied) + Logic Pro

## Relevance

Despite 0 stars, this is architecturally one of the more thoughtful projects in the full list. Key ideas:

- **Conducting metaphor** — framing gesture control as conducting rather than playing is a distinct UX philosophy; it implies broader, more expressive movements and a conductor/ensemble relationship rather than direct instrument simulation
- **Asymmetric dual-hand with semantic roles** — right = melody/lead, left = harmony/accompaniment. Same split as Hands-To-Midi (#15) and Orchesture arrived at it independently — strong convergent signal
- **KNN gesture classifier** — simpler than TensorFlow (solfege.ai) but effective for a small gesture vocabulary; fast to train at runtime
- **Gesture modifiers that alter musical meaning** (sharp, octave, minor, 7th) — compact vocabulary that punches above its weight; 3 gestures × 2 hands = 6 modifier combinations covering the most expressive musical transformations

**Limitation:** Logic Pro dependency limits it to macOS. Low owner social trust.

## Notes

- Recently active (March 10, 2026)
- KNN over MediaPipe landmarks is a lighter-weight ML alternative to TF classifiers — worth benchmarking
- The "accessible music for non-instrument players" framing is a compelling product narrative worth borrowing
