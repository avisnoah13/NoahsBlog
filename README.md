# Noah's Blog

Personal blog — engineering projects and reading list. Live at
https://noahavis.com

## Tech stack

Astro + React islands, Markdown content collections, deployed via
GitHub Actions to GitHub Pages.

## Prerequisites

Node.js `>=22.12.0` (see `engines` in `package.json`). On a fresh
computer that doesn't have it yet:

- **Windows:** `winget install OpenJS.NodeJS.LTS`
- **macOS:** `brew install node`
- Or download an installer from https://nodejs.org

Check with `node --version` (and open a new terminal after installing
— an already-open shell won't pick up the updated PATH).

## Local development

```sh
git clone https://github.com/avisnoah13/NoahsBlog.git
cd NoahsBlog
npm install
npm run dev
```

Open http://localhost:4321

## Build & preview a production build

```sh
npm run build
npm run preview
```

## Adding a new project post

1. Copy `src/content/posts/_template/` to
   `src/content/posts/<your-slug>/`.
2. Fill in the frontmatter in `index.md` (title, date, summary, and
   an optional `heroImage`).
3. Put images in `src/content/posts/<your-slug>/images/` and
   reference them with `![alt text](./images/your-image.png)`.
4. For a downloadable file (PDF, etc.) instead of an image: put it in
   `public/files/<your-slug>/` and link with an absolute path, e.g.
   `/files/<your-slug>/report.pdf`.
5. Commit and push to `main` — GitHub Actions builds and deploys
   automatically within a minute or two.

## Adding a new reading-list entry

1. Copy `src/content/books/_template/` to
   `src/content/books/<your-slug>/`.
2. Fill in the frontmatter (title, date, summary, cover, status).
3. Replace the placeholder `cover.jpg` with your book's cover image
   (same folder, same filename referenced by `cover:` in frontmatter).
4. Write the body using the `## Why I Read This` / `## What I Learned`
   sections. Set `status: in-progress` while still reading; change to
   `status: finished` when done.
5. Commit and push — deploys automatically.

## Design tokens

Colors, type scale, and spacing live in `src/styles/global.css`.

## Deployment

Pushes to `main` trigger `.github/workflows/deploy.yml`, which builds
the site and publishes it via GitHub Pages. `public/CNAME` (containing
`noahavis.com`) must not be deleted — it's what keeps the custom
domain wired up on every deploy.

First-time repo setup (one-time, when the repo is first connected to
GitHub): under Settings → Pages, set the source to "GitHub Actions",
and confirm the custom domain shows up under "Custom domain" after
the first successful deploy.
