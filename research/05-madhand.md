# MadHand

**Repo:** https://github.com/itsmadson/MadHand
**Owner:** itsmadson (50 followers)
**Stars:** 6
**Language:** Python
**Last Updated:** 2026-02-11

## What It Is

A MediaPipe-based MIDI controller where vertical position of the index finger controls the note and the thumb controls velocity. Making a fist holds the current note. Has both a GUI (PyQt5) and a CLI script version. Provides pre-built binary releases for multiple OSes.

**Stack:** MediaPipe + OpenCV + Mido + NumPy + PyQt5 + loopMIDI

**Key controls:**
- Index finger Y position → MIDI note (configurable range)
- Thumb → velocity
- Fist → hold note
- Adjustable note range, smoothing, multi-channel output

## Relevance

One of the more polished projects in this list: has a GUI, pre-built releases, adjustable parameters, and multi-channel support. The "fist to hold" interaction is a nice gesture primitive worth considering.

Good reference for:
- Continuous position → note mapping (vs discrete finger-up/down)
- GUI wrapper pattern (PyQt5) around a script core
- Providing pre-built releases alongside source

**Limitation:** Only tracks one finger's Y-axis for pitch — limited gesture vocabulary. loopMIDI dependency is Windows-centric (though Mido works cross-platform with IAC on macOS).

## Notes

- Clean architecture: separate GUI and script-only versions
- Acknowledged dependencies: MediaPipe, Mido, OpenCV, loopMIDI, Vital (synth)
