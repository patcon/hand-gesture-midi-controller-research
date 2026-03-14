# handi

**Repo:** https://github.com/akx/handi
**Owner:** akx (491 followers)
**Stars:** 2
**Language:** Python
**Last Updated:** 2024-10-19

## What It Is

"Turns your hands into a MIDI controller." Minimal README ("Very much a work in progress"), but the code is structured as a clean Python package.

**Stack:** MediaPipe 0.10 + mido 1.2 + OpenCV contrib

**Package structure:**
```
handi/
├── __main__.py        # entry point
├── controller_values.py
├── cv_utils.py
├── hand_result.py     # hand landmark abstraction
├── mp_utils.py        # MediaPipe utilities
```

## Relevance

**Second-highest owner social trust of any new project in this batch (491 followers), just behind facewave.** The code structure is worth reading even without documentation — a `hand_result.py` abstraction layer over raw MediaPipe landmarks is a pattern worth borrowing.

The `mido` + MediaPipe 0.10 combination is exactly the recommended stack from the earlier research. Clean package layout with separation of CV utilities, hand result abstraction, and controller logic is well-architected for a "work in progress."

Pinned version constraints (`mediapipe~=0.10.0`) are useful — MediaPipe's Python API has had breaking changes between versions.

## Notes

- 2 stars belies the quality signal from the owner's follower count
- Worth reading `hand_result.py` and `controller_values.py` for how landmarks are abstracted into controller values
- `opencv-contrib-python` (not just `opencv-python`) — the contrib package includes extra algorithms; worth noting if we need anything from it
