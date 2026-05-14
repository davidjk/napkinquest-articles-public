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

Host: **Cloudflare Workers** with Static Assets, push-to-deploy via the GitHub integration. Every push to `main` triggers a production deploy; every PR gets a preview deploy. Workers Build is the CI build check; a broken build shows as a red deploy.

(Cloudflare merged Pages into Workers — new projects use Workers Static Assets, which serves a static `dist/` directory the same way Pages did. The standalone Pages product is in maintenance mode.)

### Repo config

`wrangler.jsonc` at the repo root declares the static-asset deploy:

```jsonc
{
  "name": "napkinquest-articles-public",
  "compatibility_date": "2026-05-14",
  "assets": { "directory": "./dist", "not_found_handling": "404-page" }
}
```

`not_found_handling: "404-page"` serves `dist/404.html` on misses (which Astro generates).

### Cloudflare Workers project settings

- **Project name**: `napkinquest-articles-public` (must match `wrangler.jsonc` `name`)
- **Build command**: `npm run build`
- **Deploy command**: `npx wrangler deploy`
- **Environment variables** (under Advanced settings → Build variables):
  - `NPM_FLAGS=--legacy-peer-deps` — required; the theme pins eslint v10 against an outdated peer range. Without this, the install step fails.
  - `NODE_VERSION=20` — Astro 5 needs ≥18.17.1, ≥20.3, or ≥22; the build env defaults to an older version.
- **Runtime variables** (set on the Worker itself, used at request time):
  - `SITE_URL` and every `PUBLIC_*` variable from `.env.example`.

Default URL: `https://napkinquest-articles-public.<account-subdomain>.workers.dev`. Production custom domain is wired via DNSimple (see below).

Once the project is connected, add the Workers Build deploy status as a required check on PRs to `main` in GitHub branch protection so a broken build blocks merge. (The check entry only appears in the required-checks picker after at least one PR has deployed against the protected branch — open a throwaway PR first if you need it to show up.)

### DNS

DNS lives at DNSimple. After picking the production hostname, point it at the Worker:

- **Subdomain** (e.g., `www.napkinquest.com`): CNAME `<subdomain>` → `napkinquest-articles-public.<account-subdomain>.workers.dev`
- **Apex** (e.g., `napkinquest.com`): ALIAS `@` → `napkinquest-articles-public.<account-subdomain>.workers.dev` (DNSimple supports ALIAS records natively)

Then in the Worker's settings: add the custom domain, and set `SITE_URL` to the production URL.
