# salvagrid

**Repo:** https://gitlab.com/unlessgames/salvagrid
**Owner:** unlessgames (GitLab followers: not exposed)
**Stars:** 1 (GitLab)
**Language:** WebGL / JavaScript
**Last Updated:** 2020-06-18
**Live demo:** https://unlessgames.gitlab.io/salvagrid
**Origin concept:** https://community.vcvrack.com/t/diy-marbles-based-physical-matrix-mixer-controller-project (Aria Salvatrice)

## What It Is

A **webcam-based MIDI grid controller** using physical objects — entirely different paradigm from hand tracking. You place a rectangular grid (drawn on paper) in front of your webcam, then put **colorful physical objects** on cells of the grid. The webcam detects which cells are occupied by color-saturated objects and sends MIDI CC 127 (on) or 0 (off) per cell.

**How it works:**
- Select grid corners by dragging on the camera image (supports skewed/trapezoid grids)
- Set grid dimensions (columns × rows)
- Tune saturation/brightness thresholds in the Detector panel
- Each cell maps to a sequential MIDI CC number; overflow wraps to the next MIDI channel
- Works with VCVRack matrix mixers, Ableton clip launching, mute control, etc.

**Setup requirements:**
- Webcam positioned overhead/angled to face the grid surface
- Desaturated background (white paper) with black-pen grid lines
- Colorful physical objects (e.g. colored building blocks) to place on cells

**Stack:** WebGL + browser Web MIDI API (runs in-browser, no install)

## Relevance

**Conceptually distinct from every other project in this list.** Not hand gesture tracking — instead it's turning physical object placement into a MIDI grid controller. This is a tangible interface approach rather than body/hand gesture.

Worth knowing because:
- Demonstrates the Web MIDI API in a working, deployed project (same path as solfege.ai)
- The physical-object-as-controller paradigm is a genuinely different interaction model — closer to a launchpad you can customize with found objects
- Live demo is accessible and testable immediately

**Limitation:** Requires physical setup (grid, objects, overhead camera angle). Not suited for the same use cases as hand-tracking projects. Last updated 2020.

## Notes

- Originated from an Aria Salvatrice VCVRack forum post — worth following Aria's work (https://aria.dog) for creative hardware/software instrument ideas
- The color-saturation detection approach (not MediaPipe/ML) is a reminder that simple CV techniques can solve real problems
