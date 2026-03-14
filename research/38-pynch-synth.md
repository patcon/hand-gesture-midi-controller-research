# Pynch-Synth

**Repo:** https://github.com/BornToDieee1029/Pynch-Synth
**Owner:** BornToDieee1029 (0 followers)
**Stars:** 1
**Language:** Python
**Last Updated:** 2025-11-22

## What It Is

A real-time gesture instrument that tracks hand gestures and sends MIDI notes to a DAW via `mido` + `python-rtmidi`. Unusually expressive gesture vocabulary for a low-profile project.

**Stack:** MediaPipe 0.10.14 + OpenCV contrib + mido + python-rtmidi + numpy + Python 3.12
**Platforms:** macOS, Linux, Raspberry Pi 4/5 (notably cross-platform)

**Gesture → MIDI mapping:**
- **Ring finger + thumb pinch** → note-on (distinct from the more common index+thumb pinch)
- **Vertical hand movement** → pitch / glide
- **Horizontal wiggle** → vibrato
- **Pitch-bend toggle** via `P` key

**Play modes:**
- Full-range (C3–C6)
- 18-key "Slice" mode with scrollable window (like a movable keyboard segment)
- Mouse-scroll piano roll (Logic Pro-style navigation)

**HUD:** Transparent overlay with color themes

## Relevance

Several things stand out despite 0 stars and 0 owner social trust:

- **Ring+thumb pinch** (not index+thumb) — a less obvious trigger that may reduce accidental triggering, since index+thumb is involved in many natural pointing gestures
- **Horizontal wiggle → vibrato** — gesture-driven vibrato is expressive and not seen in other projects; maps a *motion quality* (oscillation) rather than a position
- **18-key slice mode** — a scrollable window of 18 keys is a clever constraint: reduces the pitch space to something manageable while still allowing access to the full range by scrolling
- **Raspberry Pi support** — suggests the tracking pipeline is light enough to run on constrained hardware
- **`python-rtmidi` (not `mido` alone)** — same virtual device pattern as ejfox and Pynch-Synth confirms this is the right approach

## Notes

- The name "Pynch" is a portmanteau of Python + pinch — well-named
- Raspberry Pi support makes this interesting for embedded/hardware instrument builds
- Vibrato via wiggle is worth implementing — it's the most natural physical expression of vibrato
