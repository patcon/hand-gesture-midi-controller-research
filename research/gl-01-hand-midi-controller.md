# hand-midi-controller (ejfox)

**Repo:** https://gitlab.com/ejfox/hand-midi-controller (also mirrored at https://github.com/ejfox/hand-midi-controller)
**Owner:** ejfox — hacker-journalist; 115 GitHub followers (https://github.com/ejfox)
**Stars:** 0 (GitLab) / 3 (GitHub)
**Language:** Python
**Last Updated:** 2026-03-11 (GitHub mirror is more recently synced)

## What It Is

A highly feature-complete, real-time dual-hand MIDI CC controller using MediaPipe + OpenCV. Creates a virtual MIDI device ("HandMIDI Virtual") that appears directly in DAW MIDI inputs — no loopMIDI/IAC setup required on macOS.

**Up to 23 MIDI CC outputs** organized by hand and parameter:

| Parameter | Left Hand CC | Right Hand CC |
|-----------|-------------|--------------|
| X position | 1 | 3 |
| Y position | 2 | 4 |
| Pinch (thumb–index distance) | 5 | 6 |
| Palm openness | 7 | 8 |
| Rotation angle | 9 | 10 |
| Thumb–Middle distance | 11 | 12 |
| Thumb–Ring distance | 13 | 14 |
| Thumb–Pinky distance | 15 | 16 |
| Fist detection | 17 | 18 |
| Finger spread | 19 | 20 |
| Velocity (movement speed) | 21 | 22 |
| Both-hand distance | — | 23 |

Advanced CC outputs (11–23) are off by default; enabled via presets.

**Advanced features:**
- **Preset system** — 5 built-in presets for different use cases; JSON-configurable
- **Click-drag region selection** — define custom X/Y mapping bounds per session
- **Exponential moving average smoothing** — adjustable at runtime
- **Multi-camera support** — cycle with `V` key
- **Retina display optimized**
- **TouchDesigner integration guide** included
- **30+ FPS** target

**Stack:** MediaPipe + OpenCV + python-rtmidi (virtual device creation) + Python 3.12

**Setup:**
```bash
./setup.sh && ./run.sh
```

**Docs included:** `CONFIGURATION_GUIDE.md`, `QUICK_REFERENCE.md`, `PERFORMANCE_NOTES.md`, `TOUCHDESIGNER_INTEGRATION.md`, `example_presets.json`

## Relevance

**Most comprehensive open-source hand-MIDI project found so far.** Surpasses motion2midi (#20) in parameter count (23 vs 4) and is open source. The parameter set is thoughtfully designed — not just X/Y but also rotation, spread, fist, velocity, and inter-hand distance.

Key ideas worth borrowing:
- **Virtual MIDI device via python-rtmidi** — "HandMIDI Virtual" appears natively in DAW inputs without any driver setup; cleaner than loopMIDI/IAC
- **Velocity tracking (hand movement speed → CC)** — unique in this list; useful for drumming/expression
- **Inter-hand distance as a parameter (CC 23)** — expressive control not seen elsewhere
- **JSON preset system** — user-configurable mapping without code changes
- **TouchDesigner integration** — shows the tool isn't just DAW-focused; useful for VJ/AV performance contexts

Owner is a hacker-journalist with 115 GitHub followers — credible social signal.

## Notes

- No stars on GitLab, but quality far exceeds starred projects
- `python-rtmidi` is the key library for creating a virtual MIDI device without OS-level driver config
- `motion_line_controller.py` and `start_line.sh` suggest an alternate "motion line" control mode worth investigating
- Worth reading `IMPLEMENTATION_SUMMARY.md` for architectural decisions
