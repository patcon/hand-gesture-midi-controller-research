# solfege.ai

**Repo:** https://github.com/instrumentbible/solfege.ai
**Owner:** instrumentbible (3 followers)
**Stars:** 16
**Language:** JavaScript
**Last Updated:** 2025-11-26
**Live demo:** https://solfege.ai

## What It Is

A web app that recognizes **solfege hand signs** (do, re, mi, fa, sol, la, ti and their chromatic variants) via webcam and plays them as MIDI notes. Uses a trained ML classifier on top of MediaPipe hand landmarks, rather than simple finger-up/down rules.

**Stack:** TensorFlow.js + MediaPipe (Hands) + JZZ.js (Web MIDI API wrapper)

**Gesture vocabulary:** 17 distinct solfege hand signs → full chromatic scale (C through B)

**Architecture:**
- MediaPipe extracts hand landmarks
- TensorFlow model classifies landmark configuration into a solfege sign
- JZZ.js sends the note via Web MIDI API

## Relevance

**Most musically grounded project in the list.** Solfege hand signs are a real, taught system with semantic meaning — this makes the gesture vocabulary intuitive for musicians and music educators.

Key ideas worth borrowing:
- **ML classification over hand landmarks** — instead of writing rules ("if finger X angle > Y"), train a classifier on labelled landmark data. More robust to user variation.
- **Web MIDI API via JZZ.js** — browser-native MIDI output, no virtual MIDI driver needed (in Chrome/Edge). This is the right path for an Electron-based build.
- **Full chromatic scale coverage** — 17 signs gives access to all 12 pitch classes with some enharmonic duplicates

The live demo at https://solfege.ai means you can try it immediately.

**Limitation:** JS/web only, no Python equivalent. Gesture training data collection UX (click button → wait 1s → record 30s) is manual but functional.

## Notes

- Two named contributors: Ryan Kemmer and Josh Stovall — worth looking at their other work
- JZZ.js is worth knowing: https://github.com/jazz-soft/JZZ — browser MIDI library with good cross-browser support
- The ML training pipeline (collect landmarks → label → train TF model) is reusable for custom gesture sets
