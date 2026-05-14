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

## Deploy

Host: **Cloudflare Pages**, push-to-deploy via the GitHub integration. Every push to `main` triggers a production deploy; every PR gets a preview deploy. Pages deploy is the CI build check; a broken build shows as a red deploy.

### Cloudflare Pages project settings

- **Build command**: `npm run build`
- **Build output directory**: `dist`
- **Root directory**: (leave blank)
- **Environment variables**:
  - `NPM_FLAGS=--legacy-peer-deps` — required; the theme pins eslint v10 against an outdated peer range. Without this, the install step fails.
  - `NODE_VERSION=20` — Astro 5 needs ≥18.17.1, ≥20.3, or ≥22; Pages defaults to an older version.
  - `SITE_URL` and every `PUBLIC_*` variable from `.env.example` — set per environment (production + preview).

Pages project slug: `napkinquest-articles-public` (matches the repo). Default URL: `https://napkinquest-articles-public.pages.dev`.

Once the project is connected, add the Pages deploy status as a required check on PRs to `main` in GitHub branch protection so a broken build blocks merge. (The "Cloudflare Pages" entry only appears in the required-checks picker after at least one PR has deployed against the protected branch — open a throwaway PR first if you need it to show up.)

### DNS

DNS lives at DNSimple. After picking the production hostname, point it at the Pages project:

- **Subdomain** (e.g., `www.napkinquest.com`): CNAME `<subdomain>` → `napkinquest-articles-public.pages.dev`
- **Apex** (e.g., `napkinquest.com`): ALIAS `@` → `napkinquest-articles-public.pages.dev` (DNSimple supports ALIAS records natively)

Then in the Pages project: add the custom domain, and set `SITE_URL` to the production URL.
