# Hands-Free

**Repo:** https://github.com/carlosmbe/Hands-Free
**Owner:** carlosmbe (25 followers)
**Stars:** 7
**Language:** Swift
**Last Updated:** 2025-03-21

## What It Is

An iOS app that uses **Apple's Vision Hand Pose framework** (not MediaPipe) to detect hand gestures via the front camera and trigger MIDI chords. A pinch action (thumb touching ring or index finger) triggers chords.

**Stack:** Swift + SwiftUI + Apple Vision framework + CoreML

**Key files:**
- `MiDi.swift` — MIDI chord generation
- `ProcessingHands.swift` — Vision framework hand pose detection
- `ContentView.swift` — SwiftUI camera UI
- `CameraViewController.swift` — camera feed + Vision request coordination

**Gesture:** Thumb + ring/index finger pinch → chord (configurable per finger)

The author recommends the follow-up project [Rhythm Snap](https://github.com/carlosmbe/Rhythm-Snap) as an improved version of the same concept.

## Relevance

**Different platform, different vision framework** — the only iOS/Swift/Apple Vision project in the list. Worth noting for two reasons:

1. **Apple Vision Hand Pose** as an alternative to MediaPipe on Apple platforms — may have better performance/integration on macOS/iOS since it's native
2. **Pinch gesture** (thumb + specific finger) as the interaction primitive — same model as dirigento-cinquecento (#18), suggesting this is a natural, well-validated gesture for MIDI triggering

The author also has 25 followers — moderate social trust — and the follow-up Rhythm-Snap repo is worth checking.

## Notes

- Requires physical iOS device (no simulator support for camera)
- Chord-per-finger-pinch model is the same as dirigento-cinquecento — convergent design from two independent developers is a good signal
- [Rhythm Snap](https://github.com/carlosmbe/Rhythm-Snap) may be worth adding to the research doc
- Native Apple Vision may outperform MediaPipe on Apple Silicon for a macOS-native build
