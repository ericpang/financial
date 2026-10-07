# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A one-page marketing site for the fictional "Horizon Wealth Planning" firm. The whole site is one file, `index.html`, with CSS in a `<style>` tag and JS in a `<script>` tag. There is no framework, build step, package manager, linter or test suite. Keep it that way: no external JS/CSS files or dependencies (only Google Fonts, Unsplash and pravatar.cc are loaded remotely).

A revamped version lives in `v2/index.html` (published at `/v2/`) and follows the same single-file structure. Leave the root `index.html` unchanged so the two can be compared. v2 has a hash-based Content-Security-Policy `<meta>`: after any edit to its `<style>` or `<script>` body, run `python tools/update-csp.py`, or the browser will block the page's CSS/JS. Its FAQ markup and the `FAQPage` JSON-LD in `<head>` must stay in sync. New files the site needs must also be copied into `_site` in `.github/workflows/pages.yml`.

## Commands

- Run: open `index.html` in a browser, or serve it with `python -m http.server` from the repo root.
- Syntax-check the JS (the only automated check available): extract the `<script>` body to a temp file and run `node --check` on it.

## Architecture

`index.html` is organised as numbered, comment-bannered sections, and each concern appears in the same order in all three layers (CSS, HTML, JS). Edits to a feature usually touch all three.

- **Design tokens**: CSS custom properties in `:root` (colors `--navy`/`--gold`/`--bg`, spacing, radius, shadows, `--nav-height`). Use these instead of hard-coded values. `--nav-height` is also used for `scroll-padding-top` and the hero height, so changing the nav height updates both.
- **Responsive**: mobile-first, with overrides at `min-width: 768px` (desktop nav, form columns, footer 2-col) and `min-width: 1024px` (3-card carousel, 2-col contact, 4-col footer).
- **Carousel**: card count is driven by the `--per-view` CSS variable, set to 3 in the 1024px media query. The JS mirrors this with `matchMedia('(min-width: 1024px)')` in `perView()`. If you change the breakpoint, change both. Slide offset is `translateX(-current * 100 / perView %)`, and the dots are rebuilt on breakpoint change.
- **Scroll animations**: elements with `.reveal` get `.visible` from an IntersectionObserver. Stat numbers use a separate observer and `data-target`/`data-prefix`/`data-suffix` attributes for the count-up.
- **Enquiry form**: validation lives in the `validators` object in the JS, keyed by field `name`. Each validator writes to `#<id>-error` via `setError()`. The radio group is the exception and writes to `#contactMethod-error` directly. Adding a field means adding the input, its `-error` span, and a validator entry. On a valid submit the form card's contents are replaced with a success message (built with `textContent` for user input) after a 1.5s timeout, and the data is logged with `console.log`. Nothing is sent to a server.
- **Newsletter form** shares `EMAIL_RE` with the enquiry form.
