---
layout: page
title: Build and deploy
description: Local preview and GitHub Pages deployment instructions for Tajkart Student Hub.
permalink: /docs/DEPLOYMENT/
---

## Preview locally

Install Ruby and Bundler, then from the repository root run:

```sh
bundle install
bundle exec jekyll serve
```

Open the local address printed in the terminal. Jekyll uses the repository's configured `baseurl`, so local pages and asset links follow the same project path as GitHub Pages.

Run the repository checks before publishing:

```sh
python scripts/validate_site.py
node --check assets/js/site.js
```

## Publish with GitHub Pages

1. Push the reviewed branch to the GitHub repository.
2. In repository Settings, open **Pages** and set **Build and deployment → Source** to **GitHub Actions**.
3. Push or merge to `main`. The `pages.yml` workflow validates and builds pull requests, then deploys successful pushes to `main`.
4. In **Settings → Environments**, restrict the `github-pages` environment to the `main` branch.
5. Open the published URL: `https://shahanishashmi.github.io/tajkart-student-hub/`.

The Jekyll configuration sets the matching project `baseurl`. The deploy job receives `pages: write` and `id-token: write`; the build job keeps read-only repository access. If the repository is moved to an organisation, custom domain, or another repository name, update `url` and `baseurl` in `_config.yml` before publishing. See [GitHub's custom Pages workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) for repository-side setup details.
