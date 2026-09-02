# CLAUDE.md

Personal blog for Noah Avis — Astro + React islands, deployed to
noahavis.com via GitHub Pages (`.github/workflows/deploy.yml`).

## Dev server

Use background mode: `astro dev --background`. Manage with
`astro dev stop` / `astro dev status` / `astro dev logs`.

## Content model

Two Zod-validated collections in `src/content.config.ts`, loaded from
`src/content/{posts,books}/<slug>/index.md`. Each entry is colocated
with its own `images/` folder — there is no shared assets tree.

- **posts**: `title`, `date`, `summary` (<=200 chars), optional
  `heroImage` (relative path via `image()`), optional `sponsor`
  (`{ name, url }`).
- **books**: `title`, `date`, `summary` (<=200 chars), required
  `cover` (via `image()`), `status`: `"finished"` | `"in-progress"`
  — this drives the "In Progress" badge; don't also add prose saying
  a book is in progress, the field is the source of truth.

`_template/` in each collection is excluded from the glob loader
(`!_template/**`) — copy it to start a new entry, don't edit in
place or it'll never actually get picked up as real content.

Non-image downloadable files (PDFs, etc.) go in
`public/files/<slug>/` and get linked with an absolute path — Astro's
image pipeline only optimizes images referenced from content
collections, not arbitrary public files.

## Style

Design tokens (colors, type scale, spacing) live entirely in
`src/styles/global.css` as CSS custom properties. Reference them in
component `<style>` blocks — don't hardcode colors or sizes.

- Font: Inter Variable, self-hosted via `@fontsource-variable/inter`
  (no external font CDN).
- Palette: warm off-white / near-black, single burnt-orange accent
  (`--color-accent`). Dark mode is `[data-theme="dark"]` on `<html>`,
  toggled by `src/components/ThemeToggle.tsx` (a `client:load`
  island). The flash-of-wrong-theme fix is an inline `<script>` in
  `BaseLayout.astro`'s `<head>` — it must stay there, not move into a
  hydrated component, or dark-mode users see a light flash on load.
- `PostCard.astro` / `BookCard.astro` inside `.card-grid` are the
  standard feed layout unit; `Badge.astro` for pills (sponsor,
  in-progress).
- Astro View Transitions (`ClientRouter`) are enabled site-wide, with
  `transition:name` on hero/cover images for the grid-to-detail morph
  — keep those names stable when touching card/detail templates.
- `prefers-reduced-motion` is already handled globally; new
  animations should respect it too, not add their own escape hatch.

## Deploy

Push to `main` → GitHub Actions builds and deploys automatically.
`public/CNAME` must keep containing `noahavis.com`.
