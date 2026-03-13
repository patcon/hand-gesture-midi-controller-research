# MidiHands

**Repo:** https://github.com/kaleprabhat24/MidiHands
**Owner:** kaleprabhat24 (1 follower)
**Stars:** 3
**Language:** Python
**Last Updated:** 2026-01-10

## What It Is

Touchless gesture-based MIDI instrument using webcam. Maps each finger to chords from the C Major / A Minor scale. Works with any MIDI-compatible DAW (explicitly mentions FL Studio).

**Stack:** OpenCV + MediaPipe + cvzone + pygame.midi

**Key feature:** Explicitly targets DAW integration (FL Studio mentioned), suggesting it routes MIDI output in a way that DAWs can pick up.

## Relevance

Very similar concept to Air-Piano and hand-gesture-midi, but uses raw MediaPipe alongside cvzone (rather than cvzone alone). Uses pygame.midi like Air-Piano, but the explicit DAW integration focus is a useful framing.

Low owner social trust (1 follower). The combination of MediaPipe + cvzone is interesting — suggests using cvzone's higher-level hand detection helpers while still having MediaPipe landmarks available.

## Notes

- C Major / A Minor scale (vs Air-Piano's D major) — different default key, same paradigm
- pygame.midi for output — same limitation as Air-Piano re: DAW routing flexibility vs mido+loopMIDI
