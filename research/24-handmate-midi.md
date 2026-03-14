# Handmate-MIDI

**Repo:** https://github.com/monlim/Handmate-MIDI
**Offline version:** https://github.com/monlim/Handmate-MIDI-Offline (9 stars)
**Owner:** monlim (28 followers)
**Stars:** 58
**Language:** JavaScript
**Last Updated:** 2025-12-04
**YouTube demo:** https://youtu.be/H97t17Q_BbM

## What It Is

A web-based hand gesture → MIDI controller built on MediaPipe + WebMidi API (via [webmidijs.org](https://webmidijs.org)). Runs in-browser (Chrome/Firefox/Edge); Safari not supported. Desktop-only. Windows users need loopMIDI or VBAN-2-Midi as a virtual MIDI bridge.

Includes a MaxMSP patch (`Miditest.maxpat`) as an example of receiving the MIDI data.

An **offline version** (Handmate-MIDI-Offline, 9 stars) runs the same code via a local Node.js server (`npm install && npm start`) for environments where serving files directly from disk doesn't work.

**Stack:** MediaPipe (JS) + WebMidi.js + HTML/CSS/JS + Node.js (offline version only)

## Relevance

**Most-starred JS-based gesture-MIDI project in the full list (58 stars).** Well ahead of solfege.ai (16) and mediamime (0).

Key things worth noting:
- **WebMidi.js** ([webmidijs.org](https://webmidijs.org)) is a cleaner, more actively maintained Web MIDI wrapper than JZZ.js used by solfege.ai — worth evaluating for any web/Electron path
- **MaxMSP patch included** — shows the tool is aimed at professional music production contexts, not just demos
- The online + offline variant pattern (same codebase, local server for offline use) is a clean distribution approach for a browser-based tool
- **VBAN-2-Midi** mentioned as a Windows alternative to loopMIDI — a new tool name worth knowing

## Notes

- No description in the GitHub repo metadata — discoverability relies on the README
- The offline version separately stars (9) — total community interest is 58 + 9 = 67 across both repos
- Owner has 28 followers — moderate social trust
