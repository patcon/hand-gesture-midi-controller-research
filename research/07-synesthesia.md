# SynesthesIA

**Repo:** https://github.com/NathanKneT/SynesthesIA
**Owner:** NathanKneT (14 followers)
**Stars:** 5
**Language:** Python
**Last Updated:** 2026-01-10

## What It Is

Real-time **full-body** gesture detection → MIDI controller, using MediaPipe's pose estimation (not just hand tracking). Phase 1 prototype. OSC communication and audio triggering are stubbed but not yet functional.

**Detected gestures:**
| Gesture | Detection Method |
|---------|-----------------|
| Arms Raised | Wrist-shoulder Y ratio |
| Arms Crossed | Wrist proximity |
| T-Pose | Arm extension ratio |
| Left Arm Tap | Velocity + proximity |
| Right Arm Tap | Velocity + proximity |

**Stack:** MediaPipe (Pose) + OpenCV + OSC (partial) + Python

**Architecture:**
```
src/
├── main.py
├── tracking/body_tracker.py
├── tracking/gesture_recognition.py
├── communication/osc_manager.py
└── audio/audio_manager.py (stub)
```

## Relevance

The only project in this list that uses **full body pose** rather than just hands. This opens up a much larger gesture vocabulary (conducting motions, dance-like control, large expressive movements).

Also notable for using **OSC** as the communication layer rather than direct MIDI — OSC is more flexible and can route to tools like Max/MSP, SuperCollider, or TouchDesigner before hitting MIDI.

Good reference for:
- Body pose → gesture recognition architecture
- OSC as an intermediate protocol
- Clean modular separation of tracking, gesture recognition, and output

**Limitation:** Early-stage (Phase 1), audio/OSC layers are stubs. Low owner social trust.
