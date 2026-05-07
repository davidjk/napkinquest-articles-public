# napkinquest-articles-public

Free NapkinQuest articles plus the Astro static site that builds them.

## Layout

- `posts/` — markdown articles (free tier). Loaded by Astro from this dir at the repo root via `src/content.config.ts`.
- `assets/` — images, charts, social cards referenced from articles.
- `data/` — `.xlsx` files referenced from articles (kept under version control so readers can click through).
- `promo/` — promotional variants generated at publish time (Instagram posts, etc.).
- `src/`, `public/`, `astro.config.mjs`, etc. — Astro site (Chirping Astro theme, customized for NapkinQuest).

## Local development

```sh
cp .env.example .env       # set PUBLIC_BUTTONDOWN_USERNAME, PUBLIC_GITHUB_HANDLE, etc.
npm install --legacy-peer-deps
npm run dev                # http://localhost:4321
npm run build              # static output -> dist/
```

`--legacy-peer-deps` is required because the theme pins eslint v10 and `eslint-plugin-jsx-a11y` declares an outdated peer range. Bun resolves this loosely; npm needs the override.

## Publishing a post

From this repo, with the `nq` CLI installed (see `napkinquest-tooling`):

```sh
nq publish posts/2026-05-06-foo.md
```

Tier is inferred from the containing repo (`napkinquest-articles-public` → free). The script commits the file, pushes to GitHub, and creates a scheduled Buttondown email.

## Frontmatter

```yaml
---
title: 'Article title'
description: 'One-line summary used for cards, OG, and email description.'
pubDate: 2026-05-06
tags: [tag1, tag2]
categories: [Category]    # optional
heroImage: ./hero.png     # optional, relative to the markdown file
math: true                # optional, opt in to KaTeX
---
```

## Theme

[Chirping Astro](https://github.com/kannansuresh/chirping-astro) by Kannan Suresh, MIT-licensed. Customizations: single locale (English), Buttondown subscribe form in footer + end of post, posts read from `./posts/` rather than `./src/content/posts/`, privacy page disabled.
