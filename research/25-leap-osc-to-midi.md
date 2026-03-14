# leap-osc-to-midi

**Repo:** https://github.com/heaversm/leap-osc-to-midi
**Owner:** heaversm (131 followers)
**Stars:** 17
**Language:** none (OSCulator config/workflow)
**Last Updated:** 2026-03-08

## What It Is

An OSCulator mapping file for routing Leap Motion hand data to MIDI via OSC. Workflow:

1. **Leap Motion** → tracks finger/hand X, Y, Z positions
2. **LeapToOSC** (Processing sketch by Nick Fox-Gieg) → broadcasts positions as OSC messages
3. **OSCulator** → receives OSC, demuxes per-finger/hand coordinates, maps to MIDI note/CC
4. **Ableton Live** (or any DAW) → receives MIDI via IAC Driver

Each finger's X/Y/Z maps to MIDI parameters or notes. Z-axis crossing the center triggers note-on, with X/Y controlling velocity/pitch. All ranges configurable in OSCulator.

**Required tools:** Leap Motion hardware, LeapToOSC (Processing), OSCulator (macOS, paid), Ableton Live, IAC Driver

## Relevance

**High owner social trust (131 followers).** Not a code project — it's a configuration for a chain of proprietary/hardware tools. Similar in spirit to the Leap-Motion-to-Ableton-Live config (#11), but more detailed and with a clearer signal path.

**OSC as middleware** is the notable pattern here: Leap Motion → OSC → MIDI rather than direct MIDI output. This decoupling (gesture input produces OSC first, then OSC is remapped to MIDI) allows flexible routing and remapping without changing the gesture code. SynesthesIA (#7) uses the same approach.

Recently touched (March 2026), suggesting the owner is still active with this setup.

## Notes

- Requires Leap Motion hardware — not webcam-based
- OSCulator is macOS-only and paid — limits reproducibility
- The OSC-as-intermediate pattern is architecture worth adopting even with webcam input
- Owner's GitHub profile worth exploring for other creative-tech projects (131 followers)
