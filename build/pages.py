#!/usr/bin/env python3
from build import *
from content_services import service_pages
from content_people import PEOPLE, team_page
from content_work import work_page, contact_page, error_page

# ================================================================== HOME

def home():
    root = ""
    cards = "".join(f"""
      <a class="service-card" href="services/{s['slug']}.html" data-reveal>
        <span class="service-card__num">{s['num']}</span>
        <span class="service-card__arrow">{ICON_ARROW}</span>
        <h3>{E(cap(s['title']))}</h3>
        <p>{E(s['short'])}</p>
        <span class="service-card__lead"><strong>{E(s['lead'])}</strong>Service lead</span>
      </a>""" for s in SERVICES)

    leads = [p for p in PEOPLE if p["home"]]
    people = "".join(f"""
      <div class="person-card" data-reveal>
        <h3>{E(p['name'])}</h3><p class="role">{E(p['role'])}</p>
      </div>""" for p in leads)

    ld = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": "IntrepidX Philosophy Limited", "url": SITE + "/",
        "logo": SITE + "/assets/img/logo-reverse.png", "image": SITE + "/assets/img/og-image.jpg",
        "email": EMAIL, "telephone": [PHONE_1_TEL, PHONE_2_TEL],
        "address": {"@type": "PostalAddress", "streetAddress": "Plot 32, Bukasa Road, Muyenga",
                    "addressLocality": "Kampala", "addressCountry": "UG"},
        "description": "Consulting firm in Kampala: due diligence, investment appraisal and valuation; post-investment support; monitoring and evaluation; impact assessment; management information systems; market analysis; feasibility studies and strategic management.",
    }
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n'

    body = f"""
<main id="main">
<section class="hero" id="top">
  <div class="hero__media" aria-hidden="true">{pic(root, "towers", "", eager=True, sizes="(max-width: 860px) 100vw, 60vw")}</div>
  <div class="hero__inner">
    <div class="container">
      <div class="hero__content">
        <span class="eyebrow" data-rise>Consulting &middot; Kampala, Uganda</span>
        <h1 class="display-1 d1" data-rise>Information you can rely on.</h1>
        <p class="lead d2" data-rise>We are a consulting firm working for lenders, investors, development partners and governments. Our seven services run from feasibility studies and due diligence before an investment to monitoring, evaluation and impact assessment after it, with information systems, market analysis and strategic planning alongside.</p>
        <div class="hero__links d3" data-rise>
          <a href="about.html"><span>More</span> About who we are</a>
          <a href="services.html"><span>View</span> Our services</a>
          <a href="contact.html"><span>Talk</span> To us</a>
        </div>
      </div>
    </div>
  </div>
  <div class="hero__bar">
    <div class="container">
      <span class="tagline">Insight. Integrity. Impact.</span>
      <span class="address">Plot 32, Bukasa Road, Muyenga</span>
      <a class="scroll-cue" href="#intro">Scroll</a>
    </div>
  </div>
</section>

<section class="section section--ivory" id="intro">
  <div class="container">
    <div class="split">
      <figure class="split__media" data-reveal>
        <div class="frame">{pic(root, "team-meeting", "Colleagues in a meeting around a table", sizes="(max-width: 900px) 100vw, 40vw")}</div>
      </figure>
      <div data-reveal class="d1">
        <span class="eyebrow">Who we are</span>
        <h2 class="display-2">Independent advice, grounded in evidence</h2>
        <p class="lead mt-s">We give lenders, investors, development partners and governments information they can act on: figures checked against source documents, findings reported plainly, and recommendations the client's own staff can put to use.</p>
        <p>IntrepidX Philosophy Limited is legally incorporated in Uganda under the Companies Act 2012. The team includes an associate professor, an evaluation specialist with a PhD, four qualified accountants, an investment manager who has passed CFA Levels I and II, a survey statistician, a software developer and two associate consultants.</p>
        <p class="mt-m"><a class="link-arrow" href="about.html">More about us</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper" id="services">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">What we do</span>
      <h2 class="display-2">Seven services, each with its own lead</h2>
      <p>Each service stands on its own. Clients can use one or several, and every assignment has a named Team Leader who deals with the client and signs off the work.</p>
    </div>
    <div class="service-grid">{cards}
    </div>
    <div class="also" data-reveal>
      <div>
        <h3>We also provide</h3>
        <ul><li>Training for boards, managers and staff</li><li>Tax and regulatory advice</li><li>Reviews of financial management and internal controls</li></ul>
      </div>
      <div>
        <h3>Who our services are for</h3>
        <ul><li>Lenders, development finance institutions and impact investors</li><li>Development partners and the programmes they fund</li><li>Ministries and local governments</li><li>SACCOs, microfinance institutions and other Tier IV institutions</li><li>Cooperatives, SMEs and NGOs</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="band section" aria-labelledby="why-title">
  <div class="band__media" aria-hidden="true">{pic(root, "boardroom", "", sizes="(max-width: 900px) 100vw, 50vw")}</div>
  <div class="container">
    <div class="band__content">
      <span class="eyebrow" data-reveal>Why work with us</span>
      <h2 class="display-2" id="why-title" data-reveal>What the team brings</h2>
      <ol class="reasons">
        <li data-reveal><div><h3>A lead for each service</h3><p>Each of our seven services has a named lead, drawn from Sebyala Samuel, Prof. Atukunda Gershom, Dr. Yusuf Kiwala, Kazooba Simon and Shafiki Sabiiti.</p></div></li>
        <li data-reveal><div><h3>Experience on both sides of a loan</h3><p>An investment manager who has made and monitored loans for impact investors, and accountants who have run the finances of companies and donor-funded projects.</p></div></li>
        <li data-reveal><div><h3>Qualified accountants</h3><p>Four of the team are qualified accountants (CPA or ACCA) and one is also a certified tax adviser. Our credit lead has passed CFA Levels I and II.</p></div></li>
        <li data-reveal><div><h3>Evaluation and research depth</h3><p>An associate professor, an evaluation specialist with a PhD and a survey statistician, with work for USAID, FCDO, the Mastercard Foundation, UNCDF, Sida, GIZ and aBi programmes.</p></div></li>
        <li data-reveal><div><h3>Our own software developer</h3><p>We can design an information system and also build, connect and support the software, so recommendations turn into tools people use.</p></div></li>
        <li data-reveal><div><h3>Local knowledge</h3><p>We know Uganda's lenders, SACCOs and public bodies well, and our team has worked in Kenya, Rwanda, South Sudan and further afield.</p></div></li>
      </ol>
    </div>
  </div>
</section>

<section class="section section--ivory statement" aria-label="Our first value">
  <div class="container" data-reveal>
    <picture><source type="image/webp" srcset="assets/img/mark-color.webp"><img class="mark" src="assets/img/mark-color.png" width="360" height="268" alt="" loading="lazy"></picture>
    <blockquote>
      <p>We check figures against source documents before we use them, and we say so when a figure could not be checked.</p>
    </blockquote>
    <hr class="rule-gold">
    <cite>Accuracy &middot; the first of our five values</cite>
  </div>
</section>

<section class="section section--paper" id="work">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Current work</span>
      <h2 class="display-2">Ongoing assignments as of September 2026</h2>
      <p>Four of our current assignments. The full track record is on the Our work page.</p>
    </div>
    <div class="work-list">
      <article class="work-item" data-reveal>
        <span class="work-item__when">Ongoing</span>
        <h3>Kampani, Belgium</h3>
        <p class="work-item__role">Consultant</p>
        <p>More than 20 due diligence assignments: financial, governance, legal, technical and commercial due diligence, with valuation and investment appraisal.</p>
        <span class="tag">Due diligence, appraisal and valuation</span>
      </article>
      <article class="work-item d1" data-reveal>
        <span class="work-item__when">Ongoing</span>
        <h3>Global Social Impact Fund (GSIF), Spain</h3>
        <p class="work-item__role">Consultant</p>
        <p>Loan monitoring for more than 15 companies in GSIF's East African portfolio: reconciling lender facilities to the balance sheet, testing liquidity and tracking capital drawdowns.</p>
        <span class="tag">Post-investment support</span>
      </article>
      <article class="work-item d2" data-reveal>
        <span class="work-item__when">From September 2026</span>
        <h3>aBi Finance Limited</h3>
        <p class="work-item__role">Lead consultant</p>
        <p>A 12-month assignment helping 15 of aBi Finance's partner Tier IV financial institutions bring loan arrears under control: diagnostics and baselines, tools, training, coaching and action plans.</p>
        <span class="tag">Post-investment support, with M&amp;E</span>
      </article>
      <article class="work-item d3" data-reveal>
        <span class="work-item__when">From August 2026</span>
        <h3>aBi Finance Limited</h3>
        <p class="work-item__role">Consultant</p>
        <p>Consultancy services for institutional appraisal and monitoring of financial institutions.</p>
        <span class="tag">Due diligence and post-investment support</span>
      </article>
    </div>
    <div class="note" data-reveal>Our track record lists 35 assignments by the firm and our consultants, for clients including the Mastercard Foundation, FCDO, USAID, UNCDF, UNDP, UNFPA, Sida, aBi and World Bank-funded projects.</div>
    <p class="mt-m" data-reveal><a class="link-arrow" href="work.html">See the full track record</a></p>
  </div>
</section>

<section class="section section--ivory" id="people">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Our people</span>
      <h2 class="display-2">Who leads the work</h2>
      <p>The Managing Director, the Company Secretary and the leads of our seven services. Eleven people in all, with full CVs available on request.</p>
    </div>
    <div class="people-grid">{people}
    </div>
    <p class="mt-m" data-reveal><a class="link-arrow" href="team.html">Meet the whole team</a></p>
  </div>
</section>

<section class="section section--navy" id="how-we-work">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">How we work</span>
      <h2 class="display-2">Seven steps, adjusted to the terms of reference</h2>
    </div>
    {steps_html()}
    <p class="mt-m" data-reveal><a class="link-arrow" href="about.html#quality">How we control quality</a></p>
  </div>
</section>
{cta(root)}
</main>
"""
    write("index.html", head(root, "index.html", "IntrepidX Philosophy Limited | Consulting, Kampala",
                             "IntrepidX Philosophy Limited is a consulting firm in Kampala, Uganda: due diligence, investment appraisal and valuation; post-investment support; monitoring and evaluation; impact assessment; management information systems; market analysis; and feasibility studies and strategic management.",
                             extra) + header(root, "index.html") + body + footer(root))


STEPS = [
    ("Agree the scope", "What decision the work supports, the questions to answer, the data we need and who we should speak to."),
    ("Collect documents and data", "We request records early and design survey or interview tools where they are needed."),
    ("Check the figures", "We trace figures to source documents and cross-check them where a second source exists."),
    ("Analyse", "We look for the causes behind the numbers, build models, and test how sensitive the results are to our assumptions."),
    ("Discuss the findings", "We take draft findings back to management and stakeholders before we finalise them."),
    ("Report and hand over", "The final report and any tools are handed over to the client's staff, with training where needed."),
    ("Follow up", "Where the assignment allows, we check whether recommendations were adopted and measure results against the baseline."),
]

def steps_html():
    return '<ol class="steps">' + "".join(
        f'<li data-reveal class="d{i % 4}"><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d) in enumerate(STEPS)) + "</ol>"


# ================================================================== ABOUT

def about():
    root = ""
    credits = "".join(
        f'<li>{E(m["title"])}: photo by {E(m["photographer"])}</li>'
        for n, m in META.items())
    body = f"""
<main id="main">
{page_hero(root, "kampala", "Kampala skyline",
           [("index.html", "Home"), (None, "About")], "About us", "About IntrepidX",
           "IntrepidX Philosophy Limited is a consulting firm in Kampala, Uganda, with seven lines of business. Each is a service in its own right, with its own lead.")}

<section class="section section--ivory">
  <div class="container">
    <div class="intro-grid">
      <div data-reveal>
        <span class="eyebrow">Who we are</span>
        <h2 class="display-2">Experienced people, seven services</h2>
        <div class="prose mt-s">
          <p>Our seven lines of business are due diligence, investment appraisal and valuation; post-investment support; monitoring and evaluation; impact assessment; management information systems; market analysis; and feasibility studies and strategic management. Our work is aimed at lenders and investors, development partners and the programmes they fund, government bodies, and financial institutions such as SACCOs and microfinance institutions.</p>
          <p>IntrepidX is legally incorporated in Uganda under the Companies Act 2012. The Managing Director, Prof. Atukunda Gershom, is an associate professor with a PhD in development studies and a postgraduate diploma in monitoring and evaluation. The team also includes an evaluation specialist with a PhD, four qualified accountants (CPA and ACCA, one also a certified tax adviser), an investment manager who has passed CFA Levels I and II, a survey statistician, a software developer and two associate consultants.</p>
          <p>Our <a href="work.html">track record</a> lists 35 assignments by the firm and our consultants, for clients including the Mastercard Foundation, FCDO, USAID, UNCDF, UNDP, UNFPA, Sida, aBi, World Bank-funded projects, government bodies, Tier IV financial institutions, and the impact investors Global Social Impact Fund in Spain, the Segal Family Foundation in New Jersey and Kampani in Belgium.</p>
          <p>Projects include more than 20 due diligence assignments for Kampani, loan monitoring for more than 15 companies in GSIF's East African portfolio, delinquency management with 15 of aBi Finance's Tier IV partners, an integrated MIS for the Mastercard Foundation's SIYEP programme, a jobs tracer study for FCDO, groundwater financing for SIWI and UNCDF, and a sub-national PEFA assessment.</p>
        </div>
      </div>
      <aside data-reveal class="d1">
        <div class="lead-card">
          <div>
            <span class="role">Managing Director</span>
            <h3>Prof. Atukunda Gershom</h3>
            <p>Associate Professor and Team Leader for our monitoring and evaluation work.</p>
          </div>
        </div>
        <div class="lead-card mt-s">
          <div>
            <span class="role">Company Secretary</span>
            <h3>Dean Niwarinda</h3>
            <p>Senior Investment Analyst, Company Secretary and our lead for investment analysis.</p>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--paper" id="vision">
  <div class="container">
    <div class="vm">
      <div data-reveal><h2>Vision</h2><p>Investment, programme and public spending decisions in Africa that rest on reliable, checked information.</p></div>
      <div data-reveal class="d1"><h2>Mission</h2><p>To give lenders, investors, development partners and governments information they can rely on, through careful due diligence and valuation, practical support after investment, honest monitoring, evaluation and impact assessment, information systems that people use, sound market analysis, and feasibility studies and strategies built on evidence.</p></div>
    </div>
  </div>
</section>

<section class="section section--navy" id="values">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Our values</span>
      <h2 class="display-2">Five things we hold to</h2>
    </div>
    <div class="values">
      <div class="value" data-reveal><h3>Accuracy</h3><p>We check figures against source documents before we use them, and we say so when a figure could not be checked.</p></div>
      <div class="value d1" data-reveal><h3>Honesty</h3><p>We report what we find, including problems the client may not want to hear, and we are clear about the limits of our work.</p></div>
      <div class="value d2" data-reveal><h3>Independence</h3><p>Our advice is objective. We declare any actual or potential conflict of interest in writing as soon as we know of it.</p></div>
      <div class="value d3" data-reveal><h3>Practical results</h3><p>We build tools and plans that the client's own staff can keep using after the assignment ends.</p></div>
      <div class="value d4" data-reveal><h3>Confidentiality</h3><p>Client, borrower and beneficiary information is used only for the assignment and is handled in line with Uganda's Data Protection and Privacy Act, 2019.</p></div>
    </div>
  </div>
</section>

<section class="section section--ivory" id="approach">
  <div class="container">
    <div class="split split--reverse">
      <div class="split__media" data-reveal>
        <div class="frame frame--logo"><picture><source type="image/webp" srcset="assets/img/logo-reverse.webp"><img src="assets/img/logo-reverse.png" width="520" height="418" alt="IntrepidX Philosophy Ltd logo with the line Insight. Integrity. Impact." loading="lazy"></picture></div>
      </div>
      <div data-reveal class="d1">
        <span class="eyebrow">How we work</span>
        <h2 class="display-2">Insight. Integrity. Impact.</h2>
        <p class="lead mt-s">The line under our logo describes how we work.</p>
        <p>We take the time to understand the numbers, we report what we find, including problems a client may not want to hear, and we make sure the work gets used by the people who have to act on it.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--navy" id="how-we-work">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">How we work</span>
      <h2 class="display-2">Seven steps, adjusted to the terms of reference</h2>
      <p>Most of our assignments follow the same broad steps.</p>
    </div>
    {steps_html()}
  </div>
</section>

<section class="section section--ivory" id="quality">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Quality control</span>
      <h2 class="display-2">How we check our own work</h2>
    </div>
    <div class="quality" data-reveal>
      <div><strong>Standard tools</strong>The same checklists, templates and data tools are used across workstreams, so findings can be compared.</div>
      <div><strong>Cross-checking</strong>Important figures are checked against a second, independent source where one exists. Figures with only one source are marked.</div>
      <div><strong>A second reader</strong>Every major output is reviewed by someone other than its author and signed off by the Team Leader.</div>
      <div><strong>Facts kept apart from opinion</strong>Reports show what we verified, what we were told, and what is our own professional view.</div>
      <div><strong>Working papers</strong>Each conclusion can be traced back through the analysis to its source.</div>
      <div><strong>Limitations stated</strong>Gaps in the data and limits on the scope are set out, with the information that would close them.</div>
      <div><strong>Confidentiality</strong>Only the assignment team has access to client data, and personal data is handled under Uganda's Data Protection and Privacy Act, 2019.</div>
    </div>
  </div>
</section>

<section class="section section--paper" id="engagement">
  <div class="container">
    <div class="intro-grid">
      <div data-reveal>
        <span class="eyebrow">How clients engage us</span>
        <h2 class="display-3">As lead consultant, as consultant, or as a partner</h2>
        <dl class="details mt-s">
          <dt>Lead consultant</dt><dd>aBi Finance, 2026 (delinquency management)</dd>
          <dt>Consultant</dt><dd>Kampani and GSIF; aBi Finance, 2026 (institutional appraisal and monitoring)</dd>
          <dt>Partner</dt><dd>We can also join a consortium or act as a local, M&amp;E, MIS or research partner.</dd>
        </dl>
      </div>
      <div data-reveal class="d1">
        <span class="eyebrow">Working relationships</span>
        <p class="lead">Members of our team have worked since 2021 with Practitioners of Contemporary Philosophy Ltd (PCP), a deal-advisory practice working across East and Southern Africa.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--ivory" id="company-details">
  <div class="container">
    <div class="intro-grid">
      <div data-reveal>
        <span class="eyebrow">Company details</span>
        <h2 class="display-3">Registration and governance</h2>
        <dl class="details mt-s">
          <dt>Registered name</dt><dd>IntrepidX Philosophy Limited</dd>
          <dt>Company type</dt><dd>Private company limited by shares</dd>
          <dt>Registration</dt><dd>Legally incorporated under the Companies Act 2012 (Uganda), No. 80034404389364</dd>
          <dt>Managing Director</dt><dd>Prof. Atukunda Gershom</dd>
          <dt>Company Secretary</dt><dd>Dean Niwarinda</dd>
          <dt>Office</dt><dd>{E(ADDRESS)}</dd>
          <dt>Postal address</dt><dd>{E(POBOX)}</dd>
          <dt>Telephone</dt><dd><a href="tel:{PHONE_1_TEL}">{PHONE_1}</a> / <a href="tel:{PHONE_2_TEL}">{PHONE_2}</a></dd>
          <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
          <dt>Professional bodies</dt><dd>Team members belong to ICPAU and ACCA</dd>
          <dt>Commitments</dt><dd>Our proposals include signed declarations on confidentiality, fraud and corruption, conflicts of interest, and data protection</dd>
        </dl>
      </div>
      <div data-reveal class="d1" id="image-credits">
        <span class="eyebrow">Photo credits</span>
        <p class="muted">The photographs on this website come from <a href="https://unsplash.com" rel="noopener">Unsplash</a> and are used under the Unsplash License. We have toned them to match our colours.</p>
        <ul class="credits">{credits}</ul>
      </div>
    </div>
  </div>
</section>
{cta(root)}
</main>
"""
    write("about.html", head(root, "about.html", "About us",
                             "Who we are: a Kampala consulting firm with a team of evaluators, accountants, investment and SACCO specialists, a statistician and a software developer.")
          + header(root, "about.html") + body + footer(root))


# ================================================================== SERVICES OVERVIEW

def services_overview():
    root = ""
    rows = "".join(f"""
      <a class="service-row" href="services/{s['slug']}.html" data-reveal>
        <span class="service-row__num">{s['num']}</span>
        <h3>{E(cap(s['title']))}</h3>
        <p>{E(s['covers'])}</p>
        <span class="service-row__lead"><strong>{E(s['lead'])}</strong>Service lead</span>
      </a>""" for s in SERVICES)
    body = f"""
<main id="main">
{page_hero(root, "analysis", "Working through figures at a desk",
           [("index.html", "Home"), (None, "Services")], "What we do", "Our services",
           "We have seven lines of business. Each one stands on its own, with a named lead, and clients can use one or several.")}
<section class="section section--ivory">
  <div class="container">
    <div class="service-rows">{rows}
    </div>
    <div class="also" data-reveal>
      <div>
        <h3>We also provide</h3>
        <ul><li>Training for boards, managers and staff</li><li>Tax and regulatory advice</li><li>Reviews of financial management and internal controls</li></ul>
      </div>
      <div>
        <h3>Who our services are for</h3>
        <ul><li>Lenders, development finance institutions and impact investors</li><li>Development partners and the programmes they fund</li><li>Ministries and local governments</li><li>SACCOs, microfinance institutions and other Tier IV institutions</li><li>Cooperatives, SMEs and NGOs</li></ul>
      </div>
    </div>
  </div>
</section>
<section class="section section--paper">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">How we staff assignments</span>
      <h2 class="display-3">A named Team Leader on every assignment</h2>
      <p>Each assignment has a named Team Leader, who deals with the client and signs off every deliverable after an internal review. The rest of the team is chosen to fit the terms of reference. Legal and technical due diligence and formal valuations use associate specialists.</p>
    </div>
    <p data-reveal><a class="link-arrow" href="team.html#staffing">Who works on what</a></p>
  </div>
</section>
{cta(root)}
</main>
"""
    write("services.html", head(root, "services.html", "Our services",
                                "Seven stand-alone services: due diligence, investment appraisal and valuation; post-investment support; monitoring and evaluation; impact assessment; management information systems; market analysis; and feasibility studies and strategic management.")
          + header(root, "services.html") + body + footer(root))


# ================================================================== extras

def extras():
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    urls = ["", "about.html", "services.html"] + [f"services/{s['slug']}.html" for s in SERVICES] + ["team.html", "work.html", "contact.html"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE}/{u}</loc><lastmod>2026-09-25</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("site.webmanifest", json.dumps({
        "name": "IntrepidX Philosophy Limited", "short_name": "IntrepidX",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}],
        "theme_color": "#020a17", "background_color": "#020a17", "display": "browser"}, indent=2))


if __name__ == "__main__":
    make_variants()
    home()
    about()
    services_overview()
    service_pages()
    team_page()
    work_page()
    contact_page()
    error_page()
    extras()
