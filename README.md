# Gestural MIDI Prototypes

Research into gesture recognition via webcam as a programmable virtual MIDI controller.

The goal is to build something that can be used by others — ideally as both a reusable library and a standalone utility — using existing open-source work as a foundation rather than building from scratch.

## Goals

- Map webcam hand (and potentially face/body) gestures to MIDI signals in real time
- Output to a virtual MIDI device that any DAW can receive
- Build toward a native app (Electron, React Native, or similar)
- Potential future integration with [codespeak.dev](https://codespeak.dev/)

## Research

See [`research/`](research/) for notes on 40+ gesture-to-MIDI projects across GitHub and GitLab, including analysis of stacks, gesture vocabularies, MIDI output patterns, and architectural recommendations.

Browsable data:
- [projects.csv](https://nakamura196.github.io/csv_viewer/?u=https%3A%2F%2Fraw.githubusercontent.com%2Fpatcon%2Fhand-gesture-midi-controller-research%2Frefs%2Fheads%2Fmain%2Fprojects.csv)
- [people.csv](https://nakamura196.github.io/csv_viewer/?u=https%3A%2F%2Fraw.githubusercontent.com%2Fpatcon%2Fhand-gesture-midi-controller-research%2Frefs%2Fheads%2Fmain%2Fpeople.csv)

## Languages

Primary interest in Python, TypeScript/JS, and Rust.
