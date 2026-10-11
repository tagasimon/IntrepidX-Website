#!/usr/bin/env python3
"""Builds the static IntrepidX website into ../website.

All copy comes from the approved corporate profile (18 pages, Sept 2026).
Nothing here should be added without a source in the profile.
"""
import json, os, html
from pathlib import Path
from PIL import Image

OUT = Path(__file__).resolve().parent.parent / "public"
SITE = "https://intrepidx.biz"
META = json.load(open(Path(__file__).parent / "image-credits.json"))
VERSION = "20261011a"

E = html.escape

# ------------------------------------------------------------------ images

PHOTOS = list(META)

def make_variants():
    d = OUT / "assets/img"
    for n in PHOTOS:
        im = Image.open(d / f"{n}.jpg")
        if im.width > 800:
            s = im.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS)
            s.save(d / f"{n}-800.jpg", quality=80, optimize=True, progressive=True)
            s.save(d / f"{n}-800.webp", quality=76, method=6)

def dims(n):
    im = Image.open(OUT / f"assets/img/{n}.jpg")
    return im.width, im.height

def pic(root, n, alt, eager=False, sizes="(max-width: 860px) 100vw, 55vw"):
    w, h = dims(n)
    p = f"{root}assets/img/{n}"
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<picture>'
            f'<source type="image/webp" srcset="{p}-800.webp 800w, {p}.webp {w}w" sizes="{sizes}">'
            f'<img src="{p}.jpg" srcset="{p}-800.jpg 800w, {p}.jpg {w}w" sizes="{sizes}" width="{w}" height="{h}" alt="{E(alt)}" {load} decoding="async">'
            f'</picture>')

def credit(n):
    m = META[n]
    return f'Photo: {m["photographer"]} / Unsplash'

# ------------------------------------------------------------------ data

PHONE_1, PHONE_1_TEL = "0781 325225", "+256781325225"
PHONE_2, PHONE_2_TEL = "0393 000359", "+256393000359"
EMAIL = "info@intrepidx.biz"
ADDRESS = "Plot 32, Bukasa Road, Muyenga, Kampala"
POBOX = "P.O. Box 186072, Kampala, Uganda"

SERVICES = [
    dict(slug="due-diligence", num="01",
         title="Due diligence, investment appraisal and valuation",
         short="Financial, commercial, governance, legal and technical due diligence, investment appraisal, financial models and business valuations.",
         covers="Financial, commercial, governance, legal and technical due diligence; investment appraisal and financial models; business valuations, collateral assessment and valuation reviews.",
         lead="Sebyala Samuel", initials="SS", lead_role="Principal Consultant, Due Diligence and Credit Risk"),
    dict(slug="post-investment-support", num="02",
         title="Post-investment support",
         short="Independent monitoring of borrowers and investees, portfolio reviews, practical support to the institutions that receive finance, and turnaround plans.",
         covers="Monitoring of borrowers and investees for lenders and investors, portfolio reviews, hands-on support to the businesses and financial institutions that receive finance, and turnaround plans.",
         lead="Sebyala Samuel", initials="SS", lead_role="Principal Consultant, Due Diligence and Credit Risk"),
    dict(slug="monitoring-and-evaluation", num="03",
         title="Monitoring and evaluation",
         short="Baselines, M&E frameworks and plans, mid-term and end-line evaluations, surveys, capacity assessments and M&E training.",
         covers="Baseline studies, M&E frameworks and plans, mid-term and end-line evaluations, surveys, organisational capacity assessments, and M&E training.",
         lead="Prof. Atukunda Gershom", initials="AG", lead_role="Managing Director and Team Leader, Monitoring and Evaluation"),
    dict(slug="impact-assessment", num="04",
         title="Impact assessment",
         short="Impact evaluations, jobs and income measurement, outcome studies at end-line, and impact and ESG measurement for investors.",
         covers="Impact evaluations, jobs and income measurement, tracer studies, and impact and ESG measurement for investors and funds.",
         lead="Dr. Yusuf Kiwala", initials="YK", lead_role="Principal Consultant, Impact Assessment"),
    dict(slug="management-information-systems", num="05",
         title="Management information systems",
         short="Working out what information managers need, then designing the system, building the software, setting up dashboards and training the people who run it.",
         covers="Working out what information managers need, then designing the system, building or integrating the software, setting up dashboards and data collection, and training the people who will run it.",
         lead="Kazooba Simon", initials="KS", lead_role="Head of Management Information Systems"),
    dict(slug="market-analysis", num="06",
         title="Market analysis",
         short="Market assessments, sector and value-chain studies, segmentation, customer and product research, and policy and trade studies.",
         covers="Market assessments, sector and value-chain studies, market segmentation, customer and product research, and policy and trade studies.",
         lead="Shafiki Sabiiti", initials="SS", lead_role="Statistician and Data Analyst"),
    dict(slug="feasibility-and-strategy", num="07",
         title="Feasibility studies and strategic management",
         short="Feasibility and pre-feasibility studies, financial models and bankable proposals, strategic and business plans, board reviews and turnaround plans.",
         covers="Feasibility and pre-feasibility studies, financial models and bankable proposals, strategic and business plans, board and governance reviews, and turnaround plans.",
         lead="Dr. Yusuf Kiwala", initials="YK", lead_role="Principal Consultant, Impact Assessment"),
]
SVC = {s["slug"]: s for s in SERVICES}

NAV = [("index.html", "Home"), ("about.html", "About"), ("services.html", "Services"),
       ("team.html", "Team"), ("work.html", "Our work"), ("contact.html", "Contact")]

ICON_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'
ICON_UP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14"/><path d="m3 6 9 7 9-7"/></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>'

# ------------------------------------------------------------------ chrome

def head(root, path, title, desc, extra=""):
    canonical = f"{SITE}/{'' if path == 'index.html' else path}"
    full_title = title if path == "index.html" else f"{title} | IntrepidX Philosophy Limited"
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#020a17">
<meta property="og:type" content="website">
<meta property="og:site_name" content="IntrepidX Philosophy Limited">
<meta property="og:title" content="{E(full_title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{root}favicon-32.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="manifest" href="{root}site.webmanifest">
<link rel="preload" href="{root}assets/fonts/newsreader-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/fonts/source-sans-3-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/css/site.css?v={VERSION}">
<script src="{root}assets/js/site.js?v={VERSION}" defer></script>
{extra}</head>
"""

def cur(h, current):
    return ' aria-current="page"' if h == current else ""

def header(root, current):
    links = "".join(
        f'<a href="{root}{h}"{cur(h, current)}>{E(t)}</a>'
        for h, t in NAV[1:])
    prim = "".join(
        f'<li><a href="{root}{h}"{cur(h, current)}>{E(t)}</a></li>'
        for h, t in NAV)
    svc = "".join(f'<li><a href="{root}services/{s["slug"]}.html">{E(s["title"][0].upper() + s["title"][1:])}</a></li>' for s in SERVICES)
    return f"""<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container">
    <a class="brand" href="{root}index.html" aria-label="IntrepidX Philosophy Limited, home">
      <picture><source type="image/webp" srcset="{root}assets/img/wordmark-reverse.webp"><img src="{root}assets/img/wordmark-reverse.png" width="350" height="72" alt="IntrepidX Philosophy Ltd"></picture>
    </a>
    <div class="header-cluster">
      <nav class="header-nav" aria-label="Main">{links}</nav>
      <button class="menu-btn" type="button" data-menu-open aria-controls="site-menu" aria-expanded="false">
        Menu <span class="menu-btn__icon" aria-hidden="true"><span></span><span></span></span>
      </button>
    </div>
  </div>
</header>
<div class="menu" id="site-menu" role="dialog" aria-modal="true" aria-label="Site menu" hidden>
  <div class="menu__bg" aria-hidden="true">{pic(root, "towers-2", "", sizes="46vw")}</div>
  <div class="menu__top">
    <div class="container">
      <a class="brand" href="{root}index.html" aria-label="IntrepidX Philosophy Limited, home"><img src="{root}assets/img/wordmark-reverse.png" width="350" height="72" alt="IntrepidX Philosophy Ltd"></a>
      <button class="menu-btn menu-close" type="button" data-menu-close>Close <span class="menu-btn__icon" aria-hidden="true"><span></span><span></span></span></button>
    </div>
  </div>
  <div class="menu__body">
    <div class="container menu__grid">
      <ul class="menu__primary">{prim}</ul>
      <div class="menu__secondary">
        <h2>Services</h2>
        <ul>{svc}</ul>
        <h2>Contact</h2>
        <p class="menu__contact">{E(ADDRESS)}<br>
          <a href="tel:{PHONE_1_TEL}">{PHONE_1}</a> / <a href="tel:{PHONE_2_TEL}">{PHONE_2}</a><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </div>
  </div>
  <div class="menu__foot"><div class="container"><span>Insight. Integrity. Impact.</span><span>Kampala, Uganda</span></div></div>
</div>
"""

def footer(root):
    svc = "".join(f'<li><a href="{root}services/{s["slug"]}.html">{E(s["title"][0].upper() + s["title"][1:])}</a></li>' for s in SERVICES)
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <picture><source type="image/webp" srcset="{root}assets/img/logo-reverse.webp"><img src="{root}assets/img/logo-reverse.png" width="520" height="418" alt="IntrepidX Philosophy Ltd. Insight. Integrity. Impact." loading="lazy"></picture>
      <p>A consulting firm in Kampala, Uganda. Registration No. 80034404389364.</p>
    </div>
    <div>
      <h2>Company</h2>
      <ul>
        <li><a href="{root}about.html">About us</a></li>
        <li><a href="{root}team.html">Our team</a></li>
        <li><a href="{root}work.html">Our work</a></li>
        <li><a href="{root}contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h2>Services</h2>
      <ul>{svc}</ul>
    </div>
    <div>
      <h2>Contact</h2>
      <address>
        IntrepidX Philosophy Limited<br>
        Plot 32, Bukasa Road, Muyenga<br>
        {POBOX}<br>
        Tel: <a href="tel:{PHONE_1_TEL}">{PHONE_1}</a> / <a href="tel:{PHONE_2_TEL}">{PHONE_2}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a><br>
        <a href="mailto:dniwarinda@intrepidx.biz">dniwarinda@intrepidx.biz</a>
      </address>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <span>&copy; <span data-year>2026</span> IntrepidX Philosophy Limited</span>
      <span>Photographs from Unsplash. <a href="{root}about.html#image-credits">Photo credits</a></span>
    </div>
  </div>
</footer>
<a class="to-top" href="#top" aria-label="Back to top">{ICON_UP}</a>
</body>
</html>
"""

def cta(root, title="Discuss an assignment",
        text="To discuss an assignment or request company documents for a tender, contact the Company Secretary, Dean Niwarinda, at dniwarinda@intrepidx.biz."):
    return f"""<section class="cta" aria-labelledby="cta-title">
  <div class="cta__media" aria-hidden="true">{pic(root, "meeting", "", sizes="100vw")}</div>
  <div class="container">
    <div class="cta__content" data-reveal>
      <span class="eyebrow">Contact</span>
      <h2 class="display-2" id="cta-title">{E(title)}</h2>
      <p>{E(text)}</p>
      <div class="cta__actions">
        <a class="btn" href="mailto:dniwarinda@intrepidx.biz">{ICON_MAIL} dniwarinda@intrepidx.biz</a>
        <a class="btn btn--ghost" href="tel:{PHONE_1_TEL}">{ICON_PHONE} {PHONE_1}</a>
      </div>
    </div>
  </div>
</section>
"""

def page_hero(root, img, alt, crumbs, eyebrow, h1, lead, meta="", h1cls="display-1"):
    cr = ' <span aria-hidden="true">/</span> '.join(
        f'<a href="{root}{h}">{E(t)}</a>' if h else f'<span aria-current="page">{E(t)}</span>' for h, t in crumbs)
    return f"""<section class="page-hero" id="top">
  <div class="page-hero__media">{pic(root, img, alt, eager=True, sizes="(max-width: 860px) 100vw, 52vw")}</div>
  <div class="container">
    <div class="page-hero__content">
      <nav class="crumbs" aria-label="Breadcrumb">{cr}</nav>
      <span class="eyebrow">{eyebrow}</span>
      <h1 class="{h1cls}">{h1}</h1>
      <p class="lead">{lead}</p>
      {meta}
    </div>
  </div>
</section>
"""

def write(path, content):
    p = OUT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print("wrote", path, len(content))

def cap(s):
    return s[0].upper() + s[1:]
