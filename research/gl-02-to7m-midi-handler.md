# to7m_midi_handler

**Repo:** https://gitlab.com/to7m/to7m_midi_handler
**Owner:** to7m (GitLab followers: not exposed)
**Stars:** 0 (GitLab)
**Language:** Python
**Last Updated:** 2021-07-16

## What It Is

A personal live performance MIDI translation/routing system. Not a gesture recognition project — this is middleware that sits between MIDI inputs and outputs, transforming and routing signals.

**Architecture (from source):**
- `server.py` — central routing server
- `patches/` — patch-based signal routing (Max/MSP-style patch concept)
- `controller/` — controller input handling
- `messages/` — MIDI message types
- `velocity_curves.py` — velocity curve transformations
- `int7/` — 7-bit integer utilities (MIDI value range handling)
- `io_/` — input/output abstractions

Packaged as a proper Python library (`pyproject.toml`, `setup.cfg`).

## Relevance

Low direct relevance — not a gesture → MIDI project. The "patches" architecture (named routing configurations) is conceptually related to leapmidi's "programs" and Hands-To-Midi's "banks," but this operates purely in MIDI-land with no vision input.

The library structure and velocity_curves module could be worth borrowing if we build a MIDI post-processing layer.

## Notes

- Last updated 2021 — least recently active project in the full list
- Proper Python package structure is a good reference if we publish as a library
