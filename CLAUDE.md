# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Research and prototyping project for gesture recognition via webcam (primarily MediaPipe) mapped to a programmable virtual MIDI device. The intended output is an app using native APIs (Electron, React Native, or similar). Rust is welcome despite no prior experience. The project should be usable by others — ideally as both a reusable library and standalone utility.

## Research Priorities

When researching or recommending approaches, favor:
- MediaPipe-based gesture recognition approaches
- Python, TypeScript/JS, or Rust implementations
- Newer projects with high star counts
- Building on existing libraries rather than from scratch
- Work from GitHub users with high follower counts or other highly-starred packages (social trust signal)

## Tracking Doc

A shared Google Doc tracks relevant tweets and projects found during research:
https://docs.google.com/document/d/1vE60mXheYi223IWKxCPBhkVvElrPq1aWeoSuucTwZlU/edit?tab=t.0

- The published (no-auth) version is at: https://docs.google.com/document/d/e/2PACX-1vTBWJmIlFE14g0WN6FmJ1BgtVGDwgelAR7F7vHxlHX6B_rpI3SenlGZ1KbkjSCn0RKNgySTXRCnqzNA/pub
- When processing new projects from the doc, add a research file under `research/` and link back to the source
- The doc may update over time — check it for new entries when doing research passes

## Research Files

Each project gets its own file in `research/` (e.g. `research/04-midigesture.md`). The `research/README.md` is the index with a full table and pattern analysis. GitHub projects are numbered sequentially; GitLab projects are prefixed `gl-`; additional GitHub batches continue the numbering.

## Potential Integration

[codespeak.dev](https://codespeak.dev/) is a target integration, but not a starting priority.
