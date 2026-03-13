# Gesture-Controlled-MIDI-Theremin

**Repo:** https://github.com/ezraamanoe/Gesture-Controlled-MIDI-Theremin
**Owner:** ezraamanoe (0 followers)
**Stars:** 3
**Language:** Python
**Last Updated:** 2026-03-04

## What It Is

Real-time theremin emulation using computer vision and MIDI CC messages. Maps hand position in space (X/Y axis) to MIDI control parameters, mimicking how a theremin is played — pitch controlled by one axis, volume/expression by another.

**Stack:** Likely MediaPipe + Mido (based on description and project context)

## Relevance

The theremin mapping approach (continuous 2D hand position → MIDI CC) is a distinct and useful paradigm compared to discrete finger-up/down detection. X/Y position mapping is natural for expressive control and maps well to parameters like pitch bend, filter cutoff, vibrato depth, etc.

Low owner social trust (0 followers), but the theremin concept itself is worth studying as a gesture interaction model.

## Notes

- Newer project (touched March 2026)
- Low community signal, but theremin-style continuous mapping is a distinct and valuable pattern
- MIDI CC messages (rather than note-on/off) are the right primitive for continuous expressive control
