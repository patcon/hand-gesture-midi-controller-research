# MediaPipe

**Repo:** https://github.com/google-ai-edge/mediapipe
**Owner:** google-ai-edge (Google)
**Stars:** 34,109
**Language:** C++ (with Python, JS, Android, iOS bindings)
**Last Updated:** 2026-03-13

## What It Is

Google's cross-platform ML framework for real-time media processing. Not a gesture-to-MIDI project — this is the underlying library used by most of the other projects in this list.

Provides hand tracking, pose estimation, face detection, and more as ready-to-use solutions via a graph-based pipeline. The Python API is the most common entry point for prototyping.

## Relevance

This is the foundation. Almost every Python-based gesture project here is built on MediaPipe's `Hands` solution, which returns 21 3D landmarks per hand in real time. Starting here before looking at the other projects gives useful context for what they're all doing under the hood.

**Key capabilities relevant to this project:**
- `mediapipe.solutions.hands` — hand landmark detection (21 points, both hands)
- `mediapipe.solutions.pose` — full body pose landmarks
- Works on webcam input with minimal setup
- Python, JS, and native bindings available

## Notes

- Despite being C++ under the hood, the Python API is approachable
- The newer `MediaPipe Tasks` API (vs the legacy `Solutions` API) is the direction Google is pushing; some older tutorials use the legacy one
- No MIDI functionality — purely vision/tracking
