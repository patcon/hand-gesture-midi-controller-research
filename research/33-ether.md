# ether

**Repo:** https://github.com/JonathanSContreras/ether
**Owner:** JonathanSContreras (19 followers)
**Stars:** 0
**Language:** HTML/JavaScript
**Last Updated:** 2026-03-09

## What It Is

A browser-based gesture-controlled musical instrument — not a MIDI controller. Sound is generated internally via **Tone.js** (oscillator + effects chain); there is no MIDI output. Framed as a spiritual successor to the theremin.

**Gesture → audio mapping:**
| Gesture | Hand | Effect |
|---------|------|--------|
| Y position | Right | Pitch (scale-quantized) |
| Y position | Left | Volume |
| Finger spread (index–pinky distance) | Right | Octave |
| Pinch (thumb–index) | Either | Sustain / note lock |
| Fist | Left | Mute |
| Both hands raised | Both | Reverb wet/dry mix |

**Audio engine:**
- Oscillator types: Sine, Triangle, Sawtooth, Square
- Scale quantization: Pentatonic (default), Major, Minor, Chromatic
- Effects chain: Reverb → Delay → Limiter
- Root note selector (A–G)

**Stack:** MediaPipe Hands (JS) + Tone.js + HTML5 Canvas + vanilla HTML/CSS/JS
No backend, no install, no framework — single file, hostable on GitHub Pages.

## Relevance

**Most artistically considered instrument design in the entire corpus.** The README reads as a product spec with a clear MVP and a "definition of done" — rare in this space. Several things worth noting:

- **Tone.js as an alternative to MIDI output** — instead of routing to a DAW, the instrument synthesizes sound directly in the browser. This is a valid and simpler path for a standalone instrument that doesn't need DAW integration.
- **Scale quantization built in** — snapping to a musical scale is a crucial UX decision that makes gesture-pitch mapping feel musical rather than chaotic. Most other projects leave this to the DAW.
- **Both hands raised = reverb** — using *relative position of two hands* as a parameter (not just absolute position per hand) is a creative and expressive mapping not seen elsewhere.
- **Sustain/note lock via pinch** — locking a note so you can reposition your hand without changing pitch is a key ergonomic insight for gestural instruments.

The self-contained instrument approach (no MIDI) trades DAW flexibility for zero-friction UX — worth considering as a demo or onboarding mode even if the core product targets MIDI.

## Notes

- Still in MVP phase (checkboxes unchecked in README)
- Tone.js: https://tonejs.github.io/ — the standard Web Audio synthesis library; worth knowing
- The "no install, open and play" philosophy is the right UX goal for accessibility
