# Horizon Wealth Planning

A one-page marketing site for the fictional "Horizon Wealth Planning" firm, offering retirement, investment and insurance planning.

**Live demo:** https://ericpang.github.io/financial/

## Features

- Hero section with animated count-up stats (years of experience, clients, assets advised)
- Testimonials carousel (3 cards per view on desktop, with dot navigation)
- Enquiry form with client-side validation, including a preferred-contact-method radio group
- Newsletter sign-up form
- Scroll-reveal animations
- Responsive, mobile-first layout with a desktop navigation

## Tech notes

- The whole site is a single `index.html` with CSS in a `<style>` tag and JS in a `<script>` tag.
- No framework, build step, package manager or dependencies.
- Only Google Fonts, Unsplash and pravatar.cc are loaded remotely.

## Run locally

Open `index.html` in a browser, or serve it from the repo root:

```
python -m http.server
```

## Deployment

A GitHub Actions workflow (`.github/workflows/pages.yml`) deploys the site to GitHub Pages on every push to `main`.

## Demo only

The enquiry and newsletter forms are demo-only. Submissions are validated in the browser and logged to the console; nothing is sent to a server.
