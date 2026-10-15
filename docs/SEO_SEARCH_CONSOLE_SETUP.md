---
layout: page
title: Search Console and webmaster setup
description: Owner checklist for verifying the Tajkart project site, submitting its generated sitemap, and reviewing Google and Bing crawl reports.
permalink: /docs/SEO_SEARCH_CONSOLE_SETUP/
---

This is a manual owner checklist. The repository contains the Google verification file and generates a sitemap, but neither Search Console ownership nor indexing has been confirmed. The current deployed site still returns 404 for the verification URL; wait until an authorized deployment makes it publicly available before clicking **Verify**.

## Google Search Console

### 1. Add the project URL-prefix property

Open [Google Search Console](https://search.google.com/search-console), choose **Add property → URL-prefix**, and enter:

```text
https://shahanishashmi.github.io/tajkart-student-hub/
```

Use URL-prefix for this GitHub Pages project path. The repository owner does not control DNS for `github.io`, so a Domain property for that host is not appropriate.

### 2. Verify with the supplied HTML file

Choose the HTML file method. After the site is published, open:

```text
https://shahanishashmi.github.io/tajkart-student-hub/googlef0a0d65fc3e621d7.html
```

The response body must be exactly:

```text
google-site-verification: googlef0a0d65fc3e621d7.html
```

Then return to Search Console and click **Verify**. If the URL is 404, first confirm the file is present at the repository root and that the authorized Pages deployment completed. If it redirects to another host, confirm that the destination is the property being verified and that the token is still served there. Do not switch verification methods or claim ownership until Google confirms it.

### 3. Inspect the homepage

In Search Console, open **URL Inspection**, enter `https://shahanishashmi.github.io/tajkart-student-hub/`, and select **Test Live URL**. Review the reported fetch result, crawl permission, indexing permission, user-declared canonical, Google-selected canonical when available, and any redirect, robots, fetch, or indexing errors. A successful live test does not mean Google has indexed the page.

### 4. Submit the generated sitemap

After publication, submit this actual sitemap in **Sitemaps**:

```text
https://shahanishashmi.github.io/tajkart-student-hub/sitemap.xml
```

Check the processing status and discovered URL count in Search Console. The local production build is validated to generate this path, but the deployed sitemap must be checked after the relevant build is published.

### 5. Request a small number of important URLs

Once each page returns HTTP 200, has its intended canonical, and is allowed to be indexed, use URL Inspection to request indexing for the homepage and a few original learning pages such as the Python variables lesson and linear-equation modeling lesson. Repeated requests do not guarantee faster crawling or indexing.

### 6. Monitor actual reports

Review **Page indexing** and **Sitemaps** after Google has had time to crawl. Investigate statuses only when they appear in the account, including discovered or crawled but not indexed, duplicate canonical reports, robots blocks, `noindex`, redirect errors, and server errors. Do not infer Google's selected canonical, crawl status, or indexing decision from a local build or public HTTP check.

Official references: [HTML file ownership verification](https://support.google.com/webmasters/answer/9008080), [URL Inspection](https://support.google.com/webmasters/answer/9012289), and [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview).

## Bing Webmaster Tools

Open [Bing Webmaster Tools](https://www.bing.com/webmasters/), add the canonical project URL, and complete a verification method offered by Bing. Importing from Search Console may be used only if Bing currently offers it and the owner completes the flow successfully; Google verification alone is not proof of Bing verification.

After the site is published, submit `https://shahanishashmi.github.io/tajkart-student-hub/sitemap.xml`. Review Bing's URL inspection, indexing, and crawl reports, then investigate the errors actually shown there. Do not treat a sitemap submission as confirmation that Bing indexed its URLs.
