# IntrepidX Philosophy Limited: website

This is a static website served by nginx in a small Docker image. It is ready to deploy on Coolify with the **Dockerfile** build pack.

```
WEBSITE/
├── Dockerfile                  nginx:stable-alpine, serves ./public on port 80
├── nginx/
│   ├── default.conf            clean URLs, 404 page, caching, gzip, /healthz
│   └── security-headers.conf   CSP and other security headers
├── public/                     the website (this is what gets deployed)
│   ├── index.html, about.html, services.html, team.html, work.html, contact.html, 404.html
│   ├── services/               one page per service line (6)
│   ├── assets/css, js, fonts, img
│   └── robots.txt, sitemap.xml, favicons, site.webmanifest
└── build/                      optional: Python scripts that generate public/*.html
```

The `build/` folder is not needed to run the site. It is excluded from the Docker image.

## Deploy on Coolify

1. Put the contents of this folder in a Git repository, for example on GitHub or Gitea. You can use a private repository if you give Coolify a deploy key or connect it through a GitHub App.
2. In Coolify, open your project, click **+ New**, and choose the repository.
3. Set **Build Pack** to **Dockerfile**.
4. Set **Base Directory** to `/`, or to the folder that holds the `Dockerfile` if you put this folder inside a larger repository.
5. Set **Dockerfile Location** to `/Dockerfile`.
6. Set **Ports Exposes** to `80`.
7. Under **Domains**, enter `https://intrepidx.biz`. Add `https://www.intrepidx.biz` as well if you want it. Coolify's proxy requests the TLS certificate.
8. Point the domain's DNS **A** record (and `www`, if used) at the VPS's IP address.
9. Click **Deploy**.

The Dockerfile has a `HEALTHCHECK` that calls `/healthz`. Coolify reads it, or you can set the same path under **Configuration → Healthcheck**.

Once HTTPS is working on the final domain, you can uncomment the `Strict-Transport-Security` line in `nginx/security-headers.conf` and redeploy.

## Run it locally

```bash
docker build -t intrepidx-site .
docker run --rm -p 8080:80 intrepidx-site
# open http://localhost:8080
```

Or, without Docker: `cd public && python3 -m http.server 8080`. Clean URLs such as `/about` only work under nginx. The `.html` links work everywhere.

## Editing content

You can edit the pages directly in `public/`. Each page is plain HTML and uses the shared `assets/css/site.css` and `assets/js/site.js`.

If you change the header, the footer or content that repeats across pages, it is quicker to edit the generator in `build/` and regenerate:

```bash
pip install pillow
cd build && python3 pages.py     # rewrites public/*.html
```

- `build/build.py`: shared header, footer, contact details and the list of services.
- `build/pages.py`: home, about and services overview.
- `build/content_services.py`: the six service pages.
- `build/content_people.py`: team profiles and the staffing matrix.
- `build/content_work.py`: case studies, track record, sectors, contact and 404.

After you change `site.css` or `site.js`, bump `VERSION` in `build/build.py` and regenerate. Browsers cache those files for a year, and a new version number makes them fetch the new file.

## Content rules

All copy comes from the approved Corporate Profile 2026. The track record is one table under the line "Assignments carried out by IntrepidX and its consultants"; keep that line. Do not add clients, figures, testimonials or awards that are not in the profile or backed by a document.

## Contact form

The site has no server-side code. The contact form opens the visitor's email app with a message to the Company Secretary, `dniwarinda@intrepidx.biz`, already filled in. Both `dniwarinda@intrepidx.biz` and `info@intrepidx.biz` appear on the site, so both mailboxes need to exist before launch. To receive form submissions directly instead, add a form service or a small backend, and update the CSP `form-action` and `connect-src` in `nginx/security-headers.conf` to allow it.

## Images

The photographs come from Unsplash and are used under the Unsplash License (free for commercial use; credit is not required, but the site credits the photographers on the About page, `about.html#image-credits`). They are toned toward the brand navy by `build/treat.py` so pictures from different photographers sit together. `build/image-credits.json` lists each photo, its photographer and its Unsplash source.

To swap a photo, download it, run `python3 build/treat.py <source.jpg> public/assets/img/<name>`, add an entry to `image-credits.json`, and regenerate with `cd build && python3 pages.py` (this also makes the 800 px versions).

The fonts are Newsreader, Source Sans 3 and Montserrat, all under the SIL Open Font License, and they are self-hosted in `public/assets/fonts`.
