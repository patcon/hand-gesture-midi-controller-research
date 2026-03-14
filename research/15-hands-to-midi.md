# Hands-To-Midi

**Repo:** https://github.com/youngpietro/Hands-To-Midi
**Owner:** youngpietro (0 followers)
**Stars:** 0
**Language:** Python
**Last Updated:** 2025-05-22

## What It Is

A Python MediaPipe + OpenCV hand controller with one of the most sophisticated gesture vocabularies in this list. Despite 0 stars and 0 followers, the feature set is far beyond typical projects here.

**Core concept:** Left hand and right hand serve *different roles simultaneously*:
- **Left hand fingers** → chord triggers (Bank 1) or CC toggles (Banks 2–5)
- **Right hand fingers** → continuous CC values

**Advanced features:**
- **5 banks** with different left-hand modes (chord trigger vs CC toggle)
- **Bank switching** via: keyboard (`j`/`k`), two-hand gesture training, or **speech control** (`"bank one"`, `"bank two"`)
- **Live chord training** — press `t` to train new left-hand chords at runtime
- **Gesture template training** — train custom two-hand gestures for bank switching
- **Adjustable scaling and debounce**
- Toggle global and right-hand tracking modes

**Stack:** MediaPipe + OpenCV + (speech recognition library, unspecified)

## Relevance

**Most feature-rich project in the entire list** despite having no stars. The dual-hand role assignment (left = chords/toggles, right = CC) is an excellent interaction model. The bank-switching system and live training are genuinely novel in this context.

Key ideas worth borrowing:
- **Asymmetric hand roles** — left triggers notes, right controls parameters
- **Banked programs** — multiple gesture mappings selectable at runtime (mirrors leapmidi's "programs" concept)
- **Live training** — user teaches the system their gestures rather than using hardcoded ones
- **Multimodal bank switching** — gesture + speech + keyboard — robustness through redundancy

Low owner social trust, but the architecture here is ahead of the more-starred alternatives. Worth reading the source code directly.

## Notes

- Speech control suggests `speech_recognition` or `whisper` dependency — adds a platform requirement
- May 2025 last update — not the most recently active project
