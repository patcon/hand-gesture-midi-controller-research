# cntrl

**Repo:** https://github.com/cryst4lpepsi/cntrl
**Owner:** cryst4lpepsi (1 follower)
**Stars:** 0
**Language:** Python
**Last Updated:** 2026-02-18

## What It Is

A standalone desktop app that maps hand gesture landmarks to MIDI CC knob controls, primarily targeting FL Studio. Built with MediaPipe + PySide6 (Qt GUI).

**Stack:** MediaPipe + PySide6 + python-rtmidi (or loopMIDI) + Python 3.12

**Key features:**

- **Configurable mapping UI** — each slot independently configures:
  - Landmark point (0–20 — any of MediaPipe's 21 hand landmarks)
  - Gesture type: X position, Y position, or Pinch
  - MIDI CC number (0–127)
  - Invert toggle
  - Enable/disable toggle
  - Config persisted to `config/mapping.json`
- **Multi-camera support** — dropdown to select webcam
- **Tracks up to 2 hands** with pinch detection
- **Optimized pipeline**: camera thread → downscaled tracking thread → landmarks → CC values → MIDI
- **Multiple visualizer modes**: Particle Cloud, Neon Trails, Wireframe Mesh, Holographic — all CPU-optimized via low-res overlay pipeline

## Relevance

**Most flexible landmark-to-CC mapping UI in the entire corpus.** Every other project hardcodes which landmarks map to which CC values. cntrl lets the user pick any landmark point, any gesture type, and any CC number from a GUI — and saves the config to JSON.

Key things worth borrowing:
- **Mapping UI pattern** — the per-slot configuration (landmark ID × gesture type × CC#) is the right abstraction for a "programmable" gesture MIDI controller
- **Downscaled tracking thread** — running MediaPipe on a lower-resolution copy of the frame for speed while rendering the full-res preview is a good performance optimization
- **`config/mapping.json` persistence** — user configurations survive restarts without code changes

**Limitation:** Windows-tested, 0 stars, very low owner social trust. The PySide6 (Qt) dependency adds weight but gives a proper desktop GUI.

## Notes

- The visualizer modes (particle cloud, wireframe, holographic) suggest this is aimed at performers who want visual feedback, not just developers
- The pipeline architecture (camera → tracking → landmark → CC → MIDI) is clean and worth diagramming
- Interesting contrast with ejfox's hand-midi-controller (gl-01): ejfox has more CC outputs baked in; cntrl is fully user-configurable
