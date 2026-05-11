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

## Theme

[Chirping Astro](https://github.com/kannansuresh/chirping-astro) by Kannan Suresh, MIT-licensed. Customizations: single locale (English), Buttondown subscribe form in footer + end of post, posts read from `./posts/` rather than `./src/content/posts/`, privacy page disabled.
