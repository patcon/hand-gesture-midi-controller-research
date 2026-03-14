# Research

Projects sourced from the [tracking doc](https://docs.google.com/document/d/1vE60mXheYi223IWKxCPBhkVvElrPq1aWeoSuucTwZlU/edit?tab=t.0) and user-submitted GitLab finds. GitHub projects processed in doc order; GitLab projects prefixed `gl-`.

## All Projects

| # | Project | Stars | Language | Owner Followers | Priority |
|---|---------|-------|----------|-----------------|----------|
| 1 | [mediapipe](01-mediapipe.md) | 34,109 | C++/Python | Google | Foundation — read first |
| 2 | [leapmidi](02-leapmidi.md) | 23 | C++ | 325 | High — best architecture model, library-first + swappable programs |
| 3 | [Air-Piano](03-air-piano.md) | 73 | Python | 36 | High — most stars among webcam projects, clean finger→chord pattern |
| 4 | [midiGesture](04-midigesture.md) | 5 | Python | 666 | High — owner most followed, raw MediaPipe + mido |
| 5 | [MadHand](05-madhand.md) | 6 | Python | 50 | Medium — most polished small project (GUI + releases), continuous position mapping |
| 6 | [Gesture-Controlled-MIDI-Theremin](06-gesture-controlled-midi-theremin.md) | 3 | Python | 0 | Medium — theremin paradigm (2D hand position → MIDI CC) |
| 7 | [SynesthesIA](07-synesthesia.md) | 5 | Python | 14 | Medium — full-body pose, OSC intermediate layer |
| 8 | [hand-gesture-midi](08-hand-gesture-midi.md) | 2 | Python | 9 | Low — similar to Air-Piano, less polished |
| 9 | [MidiHands](09-midihands.md) | 3 | Python | 1 | Low — similar to Air-Piano, explicit DAW targeting |
| 10 | [gesture (erikparr)](10-gesture-erikparr.md) | 0 | JavaScript | 7 | Low — likely not webcam gesture recognition |
| 11 | [Leap-Motion-to-Ableton-Live](11-leap-motion-to-ableton-live.md) | 4 | none | 2 | Low — config/docs only, requires Leap Motion + closed tools |
| 12 | [GestureMidi](12-gesturemidi.md) | 0 | Python | 3 | Low — minimal info, nothing distinctive |
| 13 | [midi-mediapipe](13-midi-mediapipe.md) | 1 | Python | 9 | Low-Medium — full-body pose → Ableton, recently active |
| 14 | [mediamime](14-mediamime.md) | 0 | JavaScript | 2 | Low — JS MediaPipe→MIDI, revisit if going web/Electron |
| 15 | [Hands-To-Midi](15-hands-to-midi.md) | 0 | Python | 0 | **High** — most sophisticated feature set: dual-hand roles, banks, live training, speech |
| 16 | [Gesture-Midi (BaselJayyusi)](16-gesture-midi-basel.md) | 0 | Python | 0 | Low — nothing distinctive |
| 17 | [air-chords](17-air-chords.md) | 0 | Python | 2 | Low — same concept as Air-Piano, less documented |
| 18 | [dirigento-cinquecento](18-dirigento-cinquecento.md) | 12 | Python | 18 | **High** — MPE support (unique), uses uv, pinch trigger, TOML config |
| 19 | [solfege.ai](19-solfege-ai.md) | 16 | JavaScript | 3 | **High** — ML classifier over landmarks (not rules), JZZ.js Web MIDI, live demo |
| 20 | [motion2midi](20-motion2midi.md) | 27 | closed | 1 | **High** — most polished end-state reference, YOLO (not MediaPipe), AU/VST3 plugin |
| 21 | [PianoHands.jl](21-pianohands-jl.md) | 13 | Julia | 73 (org) | Low — not gesture input; operates on MIDI files |
| 22 | [Hands-Free](22-hands-free.md) | 7 | Swift | 25 | Medium — Apple Vision framework (native macOS/iOS alt to MediaPipe), see also Rhythm-Snap |
| 23 | [MIDI2HANDS](23-midi2hands.md) | 3 | Python | 0 | Low — not gesture input; MIDI hand-assignment classifier |

## GitLab Projects

| # | Project | Stars | Language | Owner Followers | Priority |
|---|---------|-------|----------|-----------------|----------|
| gl-1 | [hand-midi-controller (ejfox)](gl-01-hand-midi-controller.md) | 3 (GH) | Python | 115 (GH) | **High** — most comprehensive open-source hand→MIDI; 23 CC outputs, virtual device, presets, TouchDesigner docs |
| gl-2 | [to7m_midi_handler](gl-02-to7m-midi-handler.md) | 0 | Python | — | Low — MIDI routing middleware, not gesture input |
| gl-3 | [salvagrid](gl-03-salvagrid.md) | 1 | WebGL/JS | — | Medium — physical object grid controller via webcam; distinct paradigm, live demo |

## Additional GitHub Projects

| # | Project | Stars | Language | Owner Followers | Priority |
|---|---------|-------|----------|-----------------|----------|
| 24 | [Handmate-MIDI](24-handmate-midi.md) | 58 (+9 offline) | JavaScript | 28 | **High** — most-starred JS project; WebMidi.js, MaxMSP patch, online+offline variants |
| 25 | [leap-osc-to-midi](25-leap-osc-to-midi.md) | 17 | config | 131 | Medium — OSC-as-middleware pattern; Leap Motion only |
| 26 | [HandPiano](26-handpiano.md) | 3 | Python | 18 | Low — sparse docs, nothing distinctive |
| 27 | [facewave](27-facewave.md) | 3 | JavaScript | 501 | **High** — highest social trust in batch; face + hand → MIDI CC, live demo |
| 28 | [MIDIDance](28-mididance.md) | 2 | Processing | 51 | Low — 2013, historical interest only |
| 29 | [handi](29-handi.md) | 2 | Python | 491 | **High** — very high social trust; clean MediaPipe+mido package, good architecture to read |
| 30 | [midiapipe-hand](30-midiapipe-hand.md) | 0 | JavaScript | 18 | Low — no description, old |
| 31 | [Handmate-VocalLooper](31-handmate-vocallooper.md) | 0 | HTML | 0 | Low-Medium — most recently updated (Mar 13); gesture vocal looper, extends Handmate |
| 32 | [Orchesture](32-orchesture.md) | 0 | Python | 1 | Medium — conducting metaphor, asymmetric dual-hand, KNN classifier, musical modifier gestures |

## Key Patterns Observed

**MIDI output approaches:**
- `pygame.midi` — simple, no virtual port needed, but limited DAW routing
- `mido` + IAC Driver (macOS) / loopMIDI (Windows) — flexible, routes to any DAW
- `python-rtmidi` — creates a named virtual MIDI device natively (ejfox's approach); no driver setup needed
- `WebMidi.js` (webmidijs.org) — actively maintained Web MIDI wrapper; used by Handmate-MIDI (58 stars), more polished than JZZ.js
- `JZZ.js` (Web MIDI API) — browser-native, no driver needed in Chrome/Edge
- AU/VST3 plugin — most DAW-integrated, highest friction to build (motion2midi)

**Vision/tracking stacks:**
- Raw MediaPipe (`mediapipe.solutions.hands` or `.pose`) — most control
- cvzone (wraps MediaPipe) — simpler API
- YOLO — used by motion2midi, implies MediaPipe wasn't enough for their needs
- Apple Vision Hand Pose — native macOS/iOS alternative, potentially faster on Apple Silicon
- TensorFlow classifier over MediaPipe landmarks — solfege.ai's approach; more robust than hand-coded rules

**Gesture vocabularies:**
- Discrete finger up/down → chord/note (Air-Piano, MidiHands, air-chords)
- Continuous 2D hand position → MIDI CC (MadHand, Theremin, motion2midi)
- Pinch (thumb + finger) → note trigger (dirigento-cinquecento, Hands-Free) — convergently designed by two teams
- Solfege hand signs via ML classifier (solfege.ai)
- Asymmetric dual-hand: left = chords/toggles, right = CC (Hands-To-Midi)
- Full-body pose landmarks (SynesthesIA, midi-mediapipe)
- Face + hand combined (facewave) — unique; expands vocabulary to head tilt, eye/mouth openness
- Conducting metaphor: broad arm movements → melody + harmony (Orchesture) — distinct UX framing
- KNN classifier over landmarks (Orchesture) — lighter-weight than TF, fast to train at runtime

**Notable findings:**
- **MPE support**: Only dirigento-cinquecento supports MIDI Polyphonic Expression — a significant gap in other projects
- **Closed-source commercial**: motion2midi shows there's enough demand to build a product; uses YOLO not MediaPipe
- **Two projects not relevant**: PianoHands.jl and MIDI2HANDS operate on MIDI files, not gesture input
- **Rhythm-Snap**: Follow-up to Hands-Free by the same author — worth adding to tracking doc
- **ejfox/hand-midi-controller**: Now the benchmark for open-source completeness; `python-rtmidi` virtual device is the cleanest MIDI output pattern found
- **Asymmetric dual-hand (left=harmony, right=melody)** convergently designed by Hands-To-Midi (#15) and Orchesture (#32) independently — strong signal for this as the natural mapping
- **facewave + handi**: Two projects with 490+ follower owners but near-zero stars — worth reading despite low community signal
- **Handmate ecosystem**: monlim's Handmate-MIDI (58★) is being forked (Handmate-VocalLooper) — suggests active community building on it

## Recommended Starting Stack

Based on social trust + stars + recency:
- **Vision:** Raw MediaPipe (per midiGesture, owner 666 followers) — or evaluate Apple Vision on macOS
- **MIDI output:** `mido` + IAC Driver/loopMIDI — flexible DAW routing
- **Interaction model:** Pinch trigger (convergent design from dirigento-cinquecento + Hands-Free) + MPE for expressiveness
- **Gesture vocabulary design:** Study Hands-To-Midi's dual-hand + bank model; study solfege.ai's ML classifier approach for robustness
