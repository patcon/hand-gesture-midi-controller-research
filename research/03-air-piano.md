# Air-Piano

**Repo:** https://github.com/Pramzie/Air-Piano
**Owner:** Pramzie (36 followers)
**Stars:** 73
**Language:** Python
**Last Updated:** 2026-03-03

## What It Is

Real-time MIDI chord player controlled by hand gestures from a webcam. Each finger maps to a chord in the D major scale; raising a finger triggers that chord and sustains it for 2 seconds.

**Stack:** OpenCV + cvzone (HandDetector) + pygame.midi

**Chord mapping (both hands, D major scale):**
| Finger | Chord |
|--------|-------|
| Thumb | D Major (D–F#–A) |
| Index | E Minor (E–G–B) |
| Middle | F# Minor (F#–A–C#) |
| Ring | G Major (G–B–D) |
| Pinky | A Major (A–C#–E) |

## Relevance

**Highest stars** of the webcam-based projects in this list (73). Uses cvzone rather than raw MediaPipe — cvzone wraps MediaPipe's hand detection with a simpler API. Supports both left and right hands.

Good reference for:
- Simple finger-up/down → MIDI note/chord mapping pattern
- `pygame.midi` for MIDI output (cross-platform, no virtual port required for basic use)
- Sustain/release timing logic

**Limitation:** Hardcoded to D major scale, single gesture vocabulary (finger up/down only). Not designed as a library.

## Notes

- Uses `cvzone` not raw MediaPipe — worth noting since cvzone is a thin wrapper that makes the API friendlier
- `pygame.midi` is simpler than `mido` + loopMIDI but has less flexibility for routing to DAWs
