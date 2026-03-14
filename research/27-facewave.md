# facewave

**Repo:** https://github.com/johnowhitaker/facewave
**Owner:** johnowhitaker (501 followers)
**Stars:** 3
**Language:** HTML/JavaScript
**Last Updated:** 2025-12-17
**Live demo:** https://johnowhitaker.github.io/facewave/
**Alternate demo:** https://tools.johnowhitaker.com/facewave

## What It Is

A web app that maps **both face and hand tracking** to MIDI CC, running entirely in-browser via webcam. The only project in this list that incorporates face tracking alongside hand tracking.

**Stack:** MediaPipe (JS — hands + face) + Web MIDI API + HTML

**Setup:** Create a virtual MIDI loopback device (loopMIDI on Windows, IAC on macOS), select it as output in the app, then use it as input in your DAW. Tested with Roli Equator 2.

## Relevance

**Highest owner social trust of any new project in this batch (501 followers).** Despite only 3 stars, the owner's reputation warrants attention.

**Face + hand tracking together** is unique in this entire list. Face tracking opens up parameters like:
- Head tilt / nod / turn → CC
- Eye openness → CC
- Mouth openness → CC

This dramatically expands the gesture vocabulary beyond hands alone, closer to what performers do with breath controllers or expression pedals — subtle, natural movements.

The live demo is immediately accessible to try: https://johnowhitaker.github.io/facewave/

Worth reading the source (`index.html` / JS) to see how face landmarks are extracted and mapped. Owner is active on X/Twitter (@johnowhitaker) and would likely engage if contacted.

## Notes

- MediaPipe's FaceMesh provides 468 landmarks per frame — far more than the 21 hand landmarks
- Combining face + hands suggests a "full upper-body expressive controller" direction worth pursuing
- Roli Equator 2 (MPE synth) mentioned as the test target — aligns well with dirigento-cinquecento's MPE focus
