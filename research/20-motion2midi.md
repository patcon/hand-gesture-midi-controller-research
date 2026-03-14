# motion2midi

**Repo:** https://github.com/froehlicht/motion2midi
**Owner:** froehlicht (1 follower)
**Stars:** 27
**Language:** HTML (distribution repo)
**Last Updated:** 2026-03-09
**Contact:** contact@motion2midi.com

## What It Is

A **closed-source** macOS AU/VST3 DAW plugin that maps webcam hand movements to MIDI CC parameters in real time. The GitHub repo is distribution-only (no source code). Currently in beta (v0.9.2).

**Stack (inferred):** YOLO (computer vision) — notably *not* MediaPipe

**Features:**
- 4 MIDI CC outputs mapped to left hand X, left hand Y, right hand X, right hand Y positions
- Loads directly into any AU/VST3 compatible DAW (Ableton, FL Studio, Logic, etc.)
- Customizable CC numbers, mute/solo per parameter
- Toggle video feed, keypoints, skeleton, and control zones
- Per-session settings saved with DAW project
- Automatic updates
- macOS Universal (x86_64 + arm64); Windows "coming soon"

**Setup:** IAC Driver on macOS (same as dirigento-cinquecento)

## Relevance

**Highest-starred project with active development (touched March 2026).** This is the most polished end-state reference for what we're building toward — a tool that integrates directly into a musician's DAW workflow.

Key observations:
- **DAW plugin format (AU/VST3)** is the most musician-friendly distribution — no separate app to run alongside the DAW. Worth considering as a target format.
- **YOLO instead of MediaPipe** — suggests MediaPipe wasn't sufficient for their accuracy/latency requirements. Worth investigating why.
- **4 CC outputs (L/R hand × X/Y)** is minimal but covers the most expressive parameters. Simple, predictable mapping.
- **Closed source** — can't study the implementation, but the UI/UX and feature set are well-documented and serve as a target spec.

The existence of this project as a polished commercial-grade tool confirms there's real demand for this type of software.

## Notes

- Owner has only 1 follower but the project quality is well above average
- The closed-source decision may be because this is becoming a commercial product
- Worth monitoring: https://motion2midi.com for any updates or documentation
- Windows support is planned — cross-platform is achievable
