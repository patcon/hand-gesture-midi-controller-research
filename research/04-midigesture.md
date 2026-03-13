# midiGesture

**Repo:** https://github.com/jo0707/midiGesture
**Owner:** jo0707 (666 followers)
**Stars:** 5
**Language:** Python
**Last Updated:** 2026-03-12

## What It Is

Real-time hand gesture recognition → MIDI signals using raw MediaPipe + OpenCV + Mido. Outputs to a virtual MIDI port (loopMIDI on Windows) so signals can be routed to any DAW or software synth.

**Gesture vocabulary:**
- Index finger up → play note
- Index finger touches thumb → stop note
- Index finger bent → pitch modulation

**Stack:** MediaPipe + OpenCV + Mido + loopMIDI (Windows only, tested on Python 3.11)

## Relevance

**Owner has 666 followers** — highest social trust in this list by far. Worth paying close attention to the code patterns used here.

Uses `mido` for MIDI output (more flexible than pygame.midi for DAW routing). Uses loopMIDI as a virtual port — standard pattern for Windows; on macOS, IAC Driver serves the same role.

Good reference for:
- Direct MediaPipe hand landmark → MIDI mapping (no cvzone abstraction layer)
- `mido` library usage for MIDI output
- Virtual MIDI port routing pattern

**Limitation:** Windows-only (tested), minimal gesture vocabulary, still described as "in development."

## Notes

- Uses raw `mediapipe` not cvzone — more control, more boilerplate
- Topics tagged: `mediapipe`, `midi`, `opencv`, `python` — well-labeled for discoverability
- Cross-platform MIDI port handling would be the main thing to generalize
