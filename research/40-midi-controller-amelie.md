# midi-controller (amelie-schepping)

**Repo:** https://github.com/amelie-schepping/midi-controller
**Owner:** amelie-schepping (0 followers)
**Stars:** 0
**Language:** Python
**Last Updated:** 2025-10-08

## What It Is

A MediaPipe + rtmidi hand gesture MIDI controller. Uses the `mingus` music theory library alongside MediaPipe for chord generation. Comments in the source are in German.

**Stack:** MediaPipe + OpenCV + rtmidi + mingus

**Notable:** Uses `mingus` (a Python music theory library) to generate chord voicings dynamically rather than hardcoding note values. Tracks two hands simultaneously with independent left/right gesture state.

## Relevance

Still low signal overall (0 stars, 0 followers), but more interesting than the description suggested. `mingus` for chord generation is unique in this list — it means chord voicings are computed from music theory rules rather than hardcoded MIDI note numbers, which is a cleaner approach for a programmable instrument.

## Notes

- `mingus`: https://github.com/bspaans/python-mingus — Python music theory library; worth knowing for any project that needs to generate chords programmatically
- German comments suggest a student project from a German-speaking context
