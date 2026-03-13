# leapmidi

**Repo:** https://github.com/revmischa/leapmidi
**Owner:** revmischa (325 followers)
**Stars:** 23
**Language:** C++
**Last Updated:** 2026-01-09

## What It Is

A C++ **library** (not a standalone app) for gesture-based MIDI control using the Leap Motion controller. Designed to be embedded in host applications. The companion repo [LeapMIDIX](https://github.com/revmischa/leapmidix) shows usage with macOS CoreMIDI.

Core concept: users define their own gesture "programs" — sets of gesture-to-MIDI mappings that can be swapped at runtime.

## Relevance

**Higher social trust:** Owner has 325 followers, well above others in this list. Worth studying the architecture even if Leap Motion is dated hardware.

**Architectural interest:** The library-first, embeddable design with user-defined gesture programs is a good model for what this project aims to be (reusable library + standalone utility). The concept of swappable "programs" is worth borrowing.

**Limitation:** Requires Leap Motion hardware, which is not webcam-based. The gesture input layer would need to be replaced with MediaPipe, but the MIDI output and program architecture could be instructive.

## Notes

- C++ may be useful context if we go the Rust route
- Older project (originally ~2014 era), but actively touched as of Jan 2026
- No MediaPipe dependency — predates it
