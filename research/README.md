# Research

Projects sourced from the [tracking doc](https://docs.google.com/document/d/1vE60mXheYi223IWKxCPBhkVvElrPq1aWeoSuucTwZlU/edit?tab=t.0). Processed in doc order.

## Projects (1–10)

| # | Project | Stars | Language | Owner Followers | Priority |
|---|---------|-------|----------|-----------------|----------|
| 1 | [mediapipe](01-mediapipe.md) | 34,109 | C++/Python | Google | Foundation — read first |
| 2 | [leapmidi](02-leapmidi.md) | 23 | C++ | 325 | High — best architecture model, library-first design |
| 3 | [Air-Piano](03-air-piano.md) | 73 | Python | 36 | High — most stars among webcam projects, clean finger→chord pattern |
| 4 | [midiGesture](04-midigesture.md) | 5 | Python | 666 | High — owner most followed in list, raw MediaPipe + mido |
| 5 | [MadHand](05-madhand.md) | 6 | Python | 50 | Medium — most polished (GUI + releases), continuous position mapping |
| 6 | [Gesture-Controlled-MIDI-Theremin](06-gesture-controlled-midi-theremin.md) | 3 | Python | 0 | Medium — theremin paradigm (continuous 2D → MIDI CC) is distinct and useful |
| 7 | [SynesthesIA](07-synesthesia.md) | 5 | Python | 14 | Medium — only full-body pose project, uses OSC as intermediate layer |
| 8 | [hand-gesture-midi](08-hand-gesture-midi.md) | 2 | Python | 9 | Low — similar to Air-Piano, less polished |
| 9 | [MidiHands](09-midihands.md) | 3 | Python | 1 | Low — similar to Air-Piano, explicit DAW targeting |
| 10 | [gesture (erikparr)](10-gesture-erikparr.md) | 0 | JavaScript | 7 | Low — likely not webcam-based gesture recognition |

## Key Patterns Observed

**MIDI output libraries used across projects:**
- `pygame.midi` — simpler, good for standalone audio, less flexible for DAW routing
- `mido` + loopMIDI/IAC — more complex but routes to any DAW; cross-platform with the right virtual port

**Gesture detection stacks:**
- Raw MediaPipe (`mediapipe.solutions.hands`) — most control
- cvzone (wraps MediaPipe) — simpler API, less boilerplate
- Both together (MidiHands) — access to high-level helpers + raw landmarks

**Gesture vocabularies seen:**
- Discrete finger up/down → chord/note trigger (Air-Piano, hand-gesture-midi, MidiHands)
- Continuous position (X/Y/Z) → MIDI note or CC (MadHand, Theremin)
- Full-body pose landmarks (SynesthesIA)
- Hardware-specific (leapmidi — Leap Motion)

**Recommended starting stack** based on social trust + star signals:
- MediaPipe (raw) for hand tracking — per midiGesture (owner: 666 followers)
- `mido` for MIDI output — more flexible than pygame.midi
- Virtual MIDI port: IAC Driver (macOS) or loopMIDI (Windows)
