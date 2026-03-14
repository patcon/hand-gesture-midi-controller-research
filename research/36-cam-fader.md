# cam-fader

**Repo:** https://github.com/DiesIrae2807/cam-fader
**Owner:** DiesIrae2807 (2 followers)
**Stars:** 0
**Language:** Python
**Last Updated:** 2025-12-06

## What It Is

A MIDI fader controlled by webcam hand movement. Single-purpose: hand position → MIDI fader value.

**Stack:** MediaPipe 0.10.14 + OpenCV contrib + mido + python-rtmidi + sounddevice

## Relevance

Low signal — 0 stars, 2 followers. The fader concept (continuous vertical position → MIDI CC) is already well-covered by MadHand (#5) and the Gesture-Controlled-MIDI-Theremin (#6). The `sounddevice` dependency is unusual — suggests it may also do audio monitoring rather than pure MIDI output. Not worth prioritizing.
