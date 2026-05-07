# napkinquest-articles-public

Free NapkinQuest articles. Each post is markdown with frontmatter; the static site (Astro, added in step 4) builds from `posts/`.

## Layout

- `posts/` — markdown articles (free tier)
- `promo/` — promotional variants (Instagram, etc.) generated per article
- `assets/` — images, charts, social cards
- `data/` — `.xlsx` files referenced from articles

## Publishing

Use the `nq` CLI from `napkinquest-tooling`:

```sh
nq publish posts/2026-05-06-foo.md --free
```
