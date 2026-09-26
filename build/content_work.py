from build import *
from content_track import FIRM, TEAM

SECTORS = [
    ("Financial services and microfinance", "aBi Finance appraisal, monitoring and delinquency assignments (IntrepidX); Wazalendo SACCO; the IFAD-funded Rural Financial Services Programme; Uganda Bankers Association; AMIR in Rwanda"),
    ("Development and impact finance", "Due diligence for Kampani (IntrepidX); loan monitoring for GSIF (IntrepidX); Segal Family Foundation; credit guarantee structuring; UNCDF local investment finance"),
    ("Agriculture and agribusiness", "Monitoring of a commodity exporter (IntrepidX); due diligence on an agro-processor (IntrepidX); aBi evaluations; a GIZ aquaculture baseline; USAID/TechnoServe cooperative support; NAADS and NARO"),
    ("SMEs and cooperatives", "Emyooga SACCOs (Microfinance Support Centre); 125 UCCFS member SACCOs; business development services for Cordaid Rwanda"),
    ("Public sector and public finance", "Sub-national PEFA; a Ministry of Finance reporting tool; evaluation of Public Accounts Committees; a turnaround strategy for cooperatives (Ministry of Trade, Industry and Cooperatives)"),
    ("Water, climate and environment", "SIWI groundwater financing; a UNCDF groundwater finance framework; FCDO Climate Smart Jobs; an evaluation of climate adaptation work"),
    ("Health, education, youth and social protection", "Senior Citizen Grant (Expanding Social Protection); an Enabel health insurance study; SEARCH IPT; the School Health Policy; the RETI youth initiative for refugee and host communities (Mastercard Foundation)"),
    ("Manufacturing, energy and agro-industry", "ERP and automation for manufacturers; renewable energy finance"),
]

def work_page():
    root = ""
    all_rows = "".join(f'<tr><td class="title-cell">{c}</td><td><strong>{a}</strong></td><td>{s}</td></tr>' for c, a, s in [(c, a, s) for c, a, s, m in FIRM] + TEAM)
    sectors = "".join(f'<tr><td class="title-cell">{a}</td><td>{b}</td></tr>' for a, b in SECTORS)
    body = f"""
<main id="main">
{page_hero(root, "report", "Financial report with a price chart",
           [("index.html", "Home"), (None, "Our work")], "Track record", "Our work",
           "Our track record, the assignments in progress, the sectors we cover and where we have worked.")}

<section class="section section--ivory" id="contracts">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Track record</span>
      <h2 class="display-2">Our track record</h2>
      <p>Assignments carried out by IntrepidX and its consultants.</p>
    </div>

    <div class="table-wrap" data-reveal><table class="data-table"><thead><tr><th>Client</th><th>Assignment</th><th>Key output / scope</th></tr></thead><tbody>{all_rows}</tbody></table></div>
    <div class="section-head mt-l" data-reveal>
      <h2 class="display-2">Ongoing assignments as of September 2026</h2>
      <p>Three of our current assignments, described in more detail.</p>
    </div>

    <article class="case" id="case-dd" data-reveal>
      <div class="case__meta">
        <span class="service-tag">Service 1 &middot; Due diligence, appraisal and valuation</span>
        <h3>Full due diligence</h3>
        <dl>
          <dt>Client</dt><dd>Kampani, Belgium</dd>
          <dt>Subject</dt><dd>A proposed investment in an agro-industrial processor, Uganda</dd>
          <dt>Our role</dt><dd>Consultant; one of more than 20 due diligence assignments for Kampani</dd>
          <dt>Year</dt><dd>2026</dd>
        </dl>
      </div>
      <div class="case__body">
        <h4>Background</h4>
        <p>Kampani was considering an investment in a processor that had gone from several years of losses to a profit within a year of starting a new line of business. It needed to know how much of the turnaround would last and whether the numbers could be relied on.</p>
        <h4>What we did</h4>
        <p>The due diligence covered financial, governance, legal, technical and commercial matters, with a valuation and an investment appraisal. On the financial side we rebuilt five years of financial statements, traced the latest year's revenue to invoice-level records in URA's EFRIS system, recalculated the key ratios, checked the Board-approved budget line by line, and reconciled the asset register to the audited accounts and an independent valuation.</p>
        <h4>Result</h4>
        <p>The draft report showed that the year's profit depended on a few months of income from the new business and that the budget left out a material block of its own costs. It also raised questions on loan interest, tax and related parties. We recommended going ahead only on conditions: pricing based on adjusted earnings, conditions precedent, and protections in the contract.</p>
      </div>
    </article>

    <article class="case" id="case-monitoring" data-reveal>
      <div class="case__meta">
        <span class="service-tag">Service 2 &middot; Post-investment support</span>
        <h3>Loan monitoring</h3>
        <dl>
          <dt>Client</dt><dd>Global Social Impact Fund (GSIF), Spain</dd>
          <dt>Subject</dt><dd>A borrower, an agricultural commodity exporter, Uganda: one of more than 15 companies we monitor in GSIF's East African portfolio</dd>
          <dt>Our role</dt><dd>Consultant</dd>
          <dt>Status</dt><dd>Ongoing</dd>
        </dl>
      </div>
      <div class="case__body">
        <h4>Background</h4>
        <p>GSIF wanted an independent monthly view of a borrower that has loans from several development and impact lenders, a seasonal need for working capital, and a large capital project under way.</p>
        <h4>What we do</h4>
        <p>Each month we reconcile the total of the lenders' facilities to the borrowings on the balance sheet, compare current assets with working-capital borrowing, track capital drawdowns against construction in progress, and look at stock, customer concentration, commodity prices and exchange rates. Reports now end with a section on gaps in the data.</p>
        <h4>Result so far</h4>
        <p>The reports have shown that an improvement in liquidity came from new borrowing rather than from trading, flagged a sharp one-month fall in the funding left for capital spending, and pointed out that receivables were concentrated in a few customers. We also changed the method so that total loans now reconcile to the balance sheet.</p>
      </div>
    </article>

    <article class="case" id="case-delinquency" data-reveal>
      <div class="case__meta">
        <span class="service-tag">Services 2 and 3 &middot; Support, with M&amp;E</span>
        <h3>Delinquency management</h3>
        <dl>
          <dt>Client</dt><dd>aBi Finance Limited and 15 of its partner Tier IV financial institutions, Uganda</dd>
          <dt>Our role</dt><dd>Lead consultant</dd>
          <dt>Period</dt><dd>12 months from September 2026, in progress</dd>
        </dl>
      </div>
      <div class="case__body">
        <h4>Background</h4>
        <p>A significant share of aBi Finance's Tier IV partner institutions had portfolio at risk above industry norms. aBi Finance asked for a firm to work with 15 of them for 12 months to improve how they manage their loan books.</p>
        <h4>What we are doing</h4>
        <p>Loan arrears usually come from weaknesses at several points in the credit process, so the work covers the whole lending cycle. We set a baseline for each institution (PAR 1, 30 and 90, recovery rates, the quality of credit files and MIS reports), group the institutions by risk and maturity, adapt arrears ageing reports, PAR dashboards, early-warning checklists and board reporting formats to each one, and follow training with on-the-job coaching and review.</p>
        <h4>Status</h4>
        <p>Work started in September 2026. Results will be reported against each institution's baseline when the assignment closes.</p>
      </div>
    </article>
  </div>
</section>

<section class="section section--ivory" id="sectors">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Sectors</span>
      <h2 class="display-2">Where the work has been</h2>
      <p>Examples of work by the firm, marked (IntrepidX), and by members of our team before joining us or alongside it.</p>
    </div>
    <div class="table-wrap" data-reveal><table class="data-table"><thead><tr><th>Sector</th><th>Examples</th></tr></thead><tbody>{sectors}</tbody></table></div>
  </div>
</section>

<section class="section section--paper" id="countries">
  <div class="container">
    <div class="map-block">
      <figure data-reveal>
        <img src="assets/img/africa-map.svg?v=3" width="360" height="380" alt="Map of Africa showing Uganda, Kenya, Rwanda, Tanzania, South Sudan, Namibia, Mali, Senegal and South Africa" loading="lazy">
      </figure>
      <div data-reveal class="d1">
        <span class="eyebrow">Countries</span>
        <h2 class="display-2">Where we have worked</h2>
        <ul class="map-legend mt-s">
          <li><span class="swatch swatch--base" aria-hidden="true"></span><span><strong>Uganda</strong>, our base, with assignments in the Central, Western, Eastern and Northern regions and in West Nile.</span></li>
          <li><span class="swatch swatch--led" aria-hidden="true"></span><span><strong>Kenya, Rwanda, Tanzania and South Sudan</strong>, where the firm or team members have worked on assignments.</span></li>
          <li><span class="swatch swatch--team" aria-hidden="true"></span><span><strong>Namibia, Mali, Senegal and South Africa</strong>, covered by team members' assignments, and IGAD member states (a regional trade-policy assessment).</span></li>
        </ul>
        <p class="mt-s"><strong>Clients outside Africa:</strong> Kampani (Belgium), Global Social Impact Fund (Spain) and the Segal Family Foundation (New Jersey, USA).</p>
        <p class="mt-s muted">Sebyala Samuel has also worked on transactions in 15 African and 2 European markets.</p>
        <div class="note"><strong>Work in other countries.</strong> Where we have not worked before, we team up with a firm that has a local presence and say so in our proposal.</div>
      </div>
    </div>
  </div>
</section>
{cta(root)}
</main>
"""
    write("work.html", head(root, "work.html", "Our work",
                            "IntrepidX's track record and ongoing assignments, the sectors we cover and the countries where our team has worked.")
          + header(root, "work.html") + body + footer(root))


def contact_page():
    root = ""
    maps = "https://www.google.com/maps/search/?api=1&query=Plot+32+Bukasa+Road+Muyenga+Kampala"
    body = f"""
<main id="main">
{page_hero(root, "kampala-dusk", "Kampala at dusk",
           [("index.html", "Home"), (None, "Contact")], "Contact", "Contact us",
           "To discuss an assignment or request company documents for a tender, contact the Company Secretary, Dean Niwarinda, at dniwarinda@intrepidx.biz.")}
<section class="section section--ivory">
  <div class="container">
    <div class="contact-grid">
      <div data-reveal>
        <ul class="contact-list">
          <li><span class="k">Office</span><span class="v">{E(ADDRESS)}</span><br><a class="link-arrow mt-s" href="{maps}" rel="noopener">Open in Google Maps</a></li>
          <li><span class="k">Postal address</span><span class="v">{E(POBOX)}</span></li>
          <li><span class="k">Telephone</span><span class="v"><a href="tel:{PHONE_1_TEL}">{PHONE_1}</a><br><a href="tel:{PHONE_2_TEL}">{PHONE_2}</a></span></li>
          <li><span class="k">Email</span><span class="v"><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="mailto:dniwarinda@intrepidx.biz">dniwarinda@intrepidx.biz</a> (Company Secretary)</span></li>
          <li><span class="k">Contact person</span><span class="v">Dean Niwarinda, Company Secretary</span></li>
        </ul>
      </div>
      <div data-reveal class="d1">
        <span class="eyebrow">Write to us</span>
        <h2 class="display-3">Send us a message</h2>
        <p class="muted mt-s">This form opens your email app with the message filled in, addressed to Dean Niwarinda, Company Secretary (dniwarinda@intrepidx.biz). Nothing is stored on this website.</p>
        <form class="form mt-s" data-mail-form data-to="dniwarinda@intrepidx.biz" action="mailto:dniwarinda@intrepidx.biz" method="post" enctype="text/plain">
          <div class="row">
            <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="f-org">Organisation</label><input id="f-org" name="organisation" type="text" autocomplete="organization"></div>
          </div>
          <div class="row">
            <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
            <div class="field"><label for="f-phone">Telephone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
          </div>
          <div class="field">
            <label for="f-subject">Subject</label>
            <select id="f-subject" name="subject">
              <option>An assignment</option>
              <option>Company documents for a tender</option>
              <option>Request for CVs</option>
              <option>Something else</option>
            </select>
          </div>
          <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" required></textarea></div>
          <div><button class="btn btn--navy" type="submit">{ICON_MAIL} Write the email</button></div>
          <p class="hint" data-status aria-live="polite"></p>
        </form>
      </div>
    </div>
  </div>
</section>
</main>
"""
    write("contact.html", head(root, "contact.html", "Contact us",
                               f"Contact IntrepidX Philosophy Limited: {ADDRESS}. Tel {PHONE_1} / {PHONE_2}. {EMAIL}.")
          + header(root, "contact.html") + body + footer(root))


def error_page():
    root = "/"
    body = f"""
<main id="main">
<section class="hero" id="top">
  <div class="hero__media" aria-hidden="true">{pic(root, "towers", "", eager=True, sizes="60vw")}</div>
  <div class="hero__inner">
  <div class="container">
    <div class="hero__content">
      <span class="eyebrow">Error 404</span>
      <h1 class="display-1">This page could not be found.</h1>
      <p class="lead">The address may be mistyped, or the page may have moved.</p>
      <div class="hero__links">
        <a href="/"><span>Go</span> To the home page</a>
        <a href="/services.html"><span>View</span> Our services</a>
        <a href="/contact.html"><span>Talk</span> To us</a>
      </div>
    </div>
  </div>
  </div>
</section>
</main>
"""
    write("404.html", head(root, "404.html", "Page not found", "The page could not be found.")
          .replace('<link rel="canonical" href="https://intrepidx.biz/404.html">', '<meta name="robots" content="noindex">')
          + header(root, "") + body + footer(root))
