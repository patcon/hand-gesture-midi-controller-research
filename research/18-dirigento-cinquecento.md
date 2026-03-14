# dirigento-cinquecento

**Repo:** https://github.com/simonreitinger/dirigento-cinquecento
**Owner:** simonreitinger (18 followers)
**Stars:** 12
**Language:** Python
**Last Updated:** 2026-01-12

## What It Is

Play MIDI notes with hands via webcam. Pinch thumb + index finger to trigger notes. Notably supports **MPE (MIDI Polyphonic Expression)** — pitch and slide per note — which enables expressive per-finger control that standard MIDI cannot do.

**Stack:** Python 3.12 + uv + MediaPipe (implied) + Mido (implied) + IAC Driver (macOS)

**Key controls:**
- Thumb + index finger pinch → play note
- Multiple hands supported simultaneously
- MPE: pitch and slide encoded per note

**Configuration (config.local.toml):**
```toml
midi_bus_name = "IAC Driver Bus 1"
close_threshold = 0.04       # pinch sensitivity
pitch_leeway = 200
midi_range_start = 48
midi_range_end = 84
mpe_pitch_distance = 0.3
mpe_slide_distance = 0.05
mpe_channel = 2
```

**Setup:**
```shell
git clone ...
uv sync
uv run main.py
```

## Relevance

**Standout project.** Two things make this unique in the list:

1. **MPE support** — none of the other projects support MIDI Polyphonic Expression. MPE allows each note to carry its own pitch bend, pressure, and slide, enabling theremin-like expressiveness per finger rather than just on/off. This is the right primitive for truly expressive gesture instruments.

2. **Uses `uv`** — matches the user's preferred Python tooling (per CLAUDE.md global prefs). The project is immediately runnable with `uv sync && uv run main.py`.

**TOML-based config** is clean and user-friendly. Pinch gesture as the trigger is natural and avoids accidental triggering from hand position.

## Notes

- macOS-first (IAC Driver), but cross-platform virtual MIDI ports could substitute on Windows
- Worth reading source code — MPE implementation details are the most educational thing here
- See also: MadHand (#5) for comparison of continuous position vs pinch trigger
