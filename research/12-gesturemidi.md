# GestureMidi

**Repo:** https://github.com/paigecaskey/GestureMidi
**Owner:** paigecaskey (3 followers)
**Stars:** 0
**Language:** Python
**Last Updated:** 2025-12-19

## What It Is

A hand gesture controlled DJ system. Maps hand gestures to MIDI CC and note messages for controlling DJ software (Mixxx, Traktor, Serato, Virtual DJ).

**Stack:** MediaPipe + OpenCV + mido + python-rtmidi

**Gesture vocabulary (per hand, mirrored for left/right decks):**
| Gesture | MIDI Output |
|---------|------------|
| Fist | No action |
| Open hand + thumb out | Play (debounced) |
| Thumb + pinky | Volume (CC 1 / CC 11) |
| Pinky only | Low EQ (CC 2 / CC 12) |
| Index finger only | Mid EQ (CC 3 / CC 13) |
| Index + middle | High EQ (CC 4 / CC 14) |

Left hand controls left deck, right hand controls right deck. Uses virtual MIDI port (IAC on macOS, loopMIDI on Windows).

## Relevance

More substantial than the initial "no README detail" assessment suggested. The DJ control framing is distinctive — mapping gesture vocabulary to a specific real-world use case (DJ mixer controls: volume, EQ bands, play) rather than generic musical notes. The dual-hand asymmetric role (left deck / right deck) is a different split from the melody/harmony model seen in Orchesture and Hands-To-Midi.

Stack (MediaPipe + mido + python-rtmidi) matches the recommended stack from the research summary.

## Notes

- The debounce on the play button gesture is a practical UX detail worth noting — prevents accidental double-triggers from hand settling
- DJ software MIDI Learn workflow is well-documented in the README
