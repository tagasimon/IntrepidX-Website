from build import *

ANCHORS = {"Sebyala Samuel": "sebyala-samuel", "Dickson Turyahabwe": "dickson-turyahabwe", "Prof. Atukunda Gershom": "prof-atukunda-gershom", "Dr. Yusuf Kiwala": "dr-yusuf-kiwala", "Kazooba Simon": "kazooba-simon"}

EARLIER_NOTE = "The examples on this page come from work by members of our team, before joining IntrepidX or alongside it. They were not IntrepidX contracts."

def offering(title, text, experience=None):
    exp = f'<p class="experience"><strong>Experience.</strong> {experience}</p>' if experience else ""
    return f'<div class="offering" data-reveal><h3>{E(title)}</h3><p>{text}</p>{exp}</div>'

def examples_table(rows, cols=("Client or funder", "Assignment", "Team member", "Year")):
    head = f"<th>{cols[0]}</th><th>{cols[1]}</th><th>{cols[2]}</th><th class=\"num\">{cols[3]}</th>"
    body = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td class=\"num\">{d}</td></tr>" for a, b, c, d in rows)
    return f'<div class="table-wrap" data-reveal><table class="data-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'

def outputs(text):
    return f'<div class="outputs mt-l" data-reveal><h3>Typical outputs</h3><p>{text}</p></div>'

def lead_card(s, blurb):
    return f"""<aside class="lead-card" data-reveal>
  <div>
    <span class="role">Service lead</span>
    <h3>{E(s['lead'])}</h3>
    <p>{blurb}</p>
    <p class="mt-s"><a class="link-arrow" href="../team.html#{ANCHORS[s['lead']]}">Full profile</a></p>
  </div>
</aside>"""

def service_nav(i):
    prev_s = SERVICES[i - 1]
    next_s = SERVICES[(i + 1) % len(SERVICES)]
    return f"""<nav class="service-nav" aria-label="Other services">
  <a href="{prev_s['slug']}.html"><small>Previous service &middot; {prev_s['num']}</small><span>{E(cap(prev_s['title']))}</span></a>
  <a href="{next_s['slug']}.html"><small>Next service &middot; {next_s['num']}</small><span>{E(cap(next_s['title']))}</span></a>
</nav>"""

def service_page(slug, lead_para, intro_html, blurb, main_html, desc):
    root = "../"
    i = [s["slug"] for s in SERVICES].index(slug)
    s = SERVICES[i]
    meta = f'<div class="meta"><span>Service {s["num"]} of 06</span><span>Led by <strong>{E(s["lead"])}</strong></span></div>'
    body = f"""
<main id="main">
{page_hero(root, "analysis", "Working through figures at a desk",
           [("index.html", "Home"), ("services.html", "Services"), (None, cap(s['title']))],
           f"Service {s['num']}", E(cap(s['title'])), lead_para, meta, "display-1 display-1--long" if len(s["title"]) > 30 else "display-1")}
<section class="section section--ivory">
  <div class="container">
    <div class="intro-grid">
      <div class="prose" data-reveal>{intro_html}</div>
      {lead_card(s, blurb)}
    </div>
  </div>
</section>
{main_html}
<section class="section section--tight section--ivory">
  <div class="container">{service_nav(i)}</div>
</section>
{cta(root)}
</main>
"""
    path = f"services/{slug}.html"
    write(path, head(root, path, cap(s["title"]), desc) + header(root, "services.html") + body + footer(root))


def service_pages():
    # ---------------------------------------------------------- 1. Due diligence
    dd_rows = [
        ("Financial", "Historical financial statements, rebuilt from the audited accounts; quality of earnings; working capital, net debt and debt-like items; tax position and URA compliance; budgets and forecasts", "Report with adjusted earnings, issues ranked by severity, conditions precedent and outstanding information"),
        ("Commercial", "The market, customers and competitors; pricing and margins; supply chains; whether the sales and growth assumptions in the business plan are realistic", 'Assessment of the plan\'s market assumptions, with a full <a href="market-analysis.html">market study</a> where needed'),
        ("Governance", "Ownership and related parties; board make-up and oversight; management capacity; policies, credit processes, internal controls and reporting", "Governance assessment with a prioritised action plan"),
        ("Legal", "Incorporation and ownership records; licences and permits; material contracts; security over assets; litigation and regulatory compliance", "Legal due diligence report, prepared with an associate advocate"),
        ("Technical", "Plant, equipment and processes; capacity and condition; capital expenditure plans; environmental and social compliance", "Technical report, prepared with a sector specialist"),
    ]
    dd_table = '<div class="table-wrap" data-reveal><table class="data-table"><thead><tr><th>Due diligence</th><th>What we look at</th><th>What the client gets</th></tr></thead><tbody>' + "".join(
        f'<tr><td class="title-cell">{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in dd_rows) + "</tbody></table></div>"
    main = f"""
<section class="section section--paper">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Due diligence</span>
      <h2 class="display-2">Five kinds of due diligence</h2>
    </div>
    {dd_table}
    <p class="note" data-reveal>Legal and technical due diligence are carried out with qualified advocates and technical specialists engaged for each assignment, working under our Team Leader.</p>
  </div>
</section>
<section class="section section--ivory">
  <div class="container">
    <div class="offerings">
      {offering("Investment appraisal", "We prepare and review feasibility studies, financial models and business plans, and test them: how much debt a project can carry, and what happens to returns if prices, volumes or the exchange rate move.")}
      {offering("Valuation", "Business valuations based on cash-flow models, collateral assessment for credit decisions, and reviews of valuations prepared by others, reconciled to the asset register and accounts. Formal asset valuations are done with an associate registered valuer.")}
    </div>
    <div class="section-head mt-l" data-reveal>
      <span class="eyebrow">Examples from team members' earlier work</span>
    </div>
    {examples_table([
        ("UNCDF", "Guidelines for identifying and appraising income-generating projects in refugee-hosting areas, with bankable proposals and a financial model for each project in Gulu and Arua (Team Leader)", "Dr. Yusuf Kiwala", "&ndash;"),
        ("Mercy Corps and IOM", "Market assessment, financial model and business plan for a proposed e-waste cooperative in Bidi Bidi settlement (Team Leader)", "Dickson Turyahabwe", "2025"),
        ("Iungo Capital (as Investment Manager)", "Debt sizing and risk-adjusted return modelling for US$12 million of SME debt and equity transactions", "Sebyala Samuel", "2018&ndash;2020"),
        ("Government of South Sudan", "Feasibility study for the Yirol oil project", "Dr. Yusuf Kiwala", "2010"),
    ])}
    <p class="table-caption" data-reveal>{EARLIER_NOTE}</p>
  </div>
</section>"""
    service_page("due-diligence",
        "Before committing money, an investor or lender needs to know that the business is what its documents say it is, that the investment makes sense, and what it is worth. This service covers all three.",
        '<p>IntrepidX has carried out more than 20 due diligence assignments for Kampani, an institutional investor based in Belgium, covering financial, governance, legal, technical and commercial due diligence, valuation and investment appraisal. One of them is described under <a href="../work.html#case-dd">ongoing assignments</a>.</p><p>Sebyala Samuel leads this work. He is an investment manager with more than 12 years\' experience and over US$150 million of private-sector debt and equity transactions in 15 African and 2 European markets.</p>',
        "Principal Consultant, Due Diligence and Credit Risk. ACCA member; Master in Advanced Finance, IE Business School; passed CFA Levels I and II.",
        main,
        "Financial, commercial, governance, legal and technical due diligence; investment appraisal, financial models and business valuations, led by Sebyala Samuel.")

    # ---------------------------------------------------------- 2. Post-investment support
    main = f"""
<section class="section section--paper">
  <div class="container">
    <div class="offerings">
      {offering("Monitoring for lenders and investors", "Monthly or quarterly reports on a borrower or investee. We reconcile the lenders' facilities to the balance sheet, test current assets against short-term borrowing, track capital spending against loan drawdowns, and point out early signs of stress.",
                "IntrepidX monitors loans to more than 15 companies in the East African portfolio of Global Social Impact Fund (GSIF), Spain (<a href='../work.html#case-monitoring'>ongoing assignments</a>). Since August 2026 we have also been carrying out institutional appraisal and monitoring of financial institutions for aBi Finance.")}
      {offering("Portfolio reviews", "Periodic reviews of how an investment, a credit line or a whole portfolio is performing against plan: financial results, repayment, portfolio at risk, covenant compliance and progress on agreed actions.",
                "Sebyala Samuel has managed a US$25 million SME credit portfolio with portfolio at risk below 3% and, in an earlier role, introduced automated credit monitoring tools.")}
      {offering("Support to investees and partner institutions", "Practical help for the businesses, SACCOs and microfinance institutions that receive finance: credit and arrears management, financial management and internal controls, governance and board training, and business plans.",
                "Our delinquency management assignment is this kind of work: aBi Finance provides credit lines and guarantees to financial institutions, and we are helping 15 of them bring loan arrears under control (<a href='../work.html#case-delinquency'>ongoing assignments</a>). Dickson Turyahabwe has provided business development services to cooperatives under USAID/TechnoServe and Oikocredit programmes and built capacity in Oikocredit partner institutions.")}
      {offering("Turnaround and recovery", "When an investment runs into trouble: finding the causes, restructuring options, recovery plans for non-performing loans, and follow-up until the plan is working.",
                "Sebyala Samuel has worked on turnaround strategies for distressed loans with the Uganda Bankers Association since 2023. Dickson Turyahabwe worked on a national turnaround strategy for cooperatives for the Ministry of Trade, Industry and Cooperatives (2022).")}
    </div>
    {outputs("Monitoring reports with early-warning indicators, portfolio reviews, action plans for each institution, training and coaching, recovery plans, and a close-out report against the baseline.")}
  </div>
</section>"""
    service_page("post-investment-support",
        "Once the money has gone out, the lender or investor needs regular, independent information on how the investment is doing, and the business or institution that received it often needs practical help to use it well. We do both.",
        "<p>We provide this support whether or not we carried out the original due diligence.</p><p>Dickson Turyahabwe leads this work. He has more than 20 years with SACCOs, MFIs, cooperatives and SMEs in Uganda, Rwanda and Tanzania, and was the first General Manager of Wazalendo SACCO, where portfolio at risk stayed below 2%.</p>",
        "Principal Consultant, SMEs and Financial Inclusion. CPA, member of ICPAU and ICPAR; MBA, University of East London; Certified Microfinance Trainer.",
        main,
        "Monitoring of borrowers and investees, portfolio reviews, support to the institutions that receive finance, and turnaround and recovery, led by Dickson Turyahabwe.")

    # ---------------------------------------------------------- 3. M&E
    main = f"""
<section class="section section--paper">
  <div class="container">
    <p class="note mt-0" data-reveal>{EARLIER_NOTE}</p>
    <div class="offerings mt-m">
      {offering("Baseline studies", "Setting indicator values and checking that targets are realistic. Examples include baselines for 20 aBi-funded projects, for USAID's Water and Food Systems Activity, and a profile of 250 village savings and loan associations for the PROFIRA project.")}
      {offering("M&E frameworks and systems", "Theories of change, log frames, indicator definitions and M&amp;E plans, for example for the DINU programme (Office of the Prime Minister) and a joint log frame for NAADS and NARO.")}
      {offering("Mid-term and end-line evaluations", "Including an evaluation of Local Government Public Accounts Committees in 30 districts, an end-of-project evaluation in West Nile, and the end-line evaluation of 20 aBi value-chain and financial-services projects.")}
      {offering("Public sector performance", "A sub-national PEFA assessment, a sub-national credit rating, and a review of financial management arrangements in 20 World Bank-funded projects.")}
      {offering("Surveys and data collection", "Sampling, digital questionnaires (ODK, Kobo Toolbox, SurveyCTO), enumerator training and back-checks, including nationwide client-satisfaction surveys for URA and the Ministry of Gender, Labour and Social Development.")}
      {offering("Organisational capacity assessment", "Reviews of how well an organisation plans, monitors and reports, with a practical plan to close the gaps.")}
      {offering("Research studies", "Applied research on livelihoods, public services and the environment, such as a Bishop Stuart University study of community practices in conserving River Rwizi (2016 grant). Prof. Gershom has more than 30 publications and supervises PhD and master's research.")}
      {offering("Training and learning", "Training programme staff in M&amp;E, research methods and statistics, writing up lessons, and checking later whether new practices have been adopted.")}
    </div>
    
    {outputs("Inception reports and survey tools, baseline and evaluation reports, M&amp;E plans with indicator reference sheets, capacity assessment reports, dashboards, and short learning briefs.")}
  </div>
</section>"""
    service_page("monitoring-and-evaluation",
        "Programme teams and their funders need to know whether activities are on track and whether targets are being met. We set baselines, design M&amp;E frameworks and systems, carry out mid-term and end-line evaluations, and run the surveys behind them.",
        "<p>Prof. Atukunda Gershom leads this work. He is an associate professor at Bishop Stuart University, with a PhD in development studies and a postgraduate diploma in M&amp;E from Uganda Management Institute, and has coordinated the university's part of RETI, a consortium project funded by the Mastercard Foundation, since 2021.</p><p>He works with Dr. Yusuf Kiwala and with Shafiki Sabiiti, our statistician, who looks after sampling, survey tools and data quality.</p>",
        "Managing Director and Team Leader, Monitoring and Evaluation. Associate Professor; PhD in Development Studies; PGD in Monitoring and Evaluation, Uganda Management Institute.",
        main,
        "Baselines, M&E frameworks, mid-term and end-line evaluations, surveys, capacity assessments and M&E training, led by Prof. Atukunda Gershom.")

    # ---------------------------------------------------------- 4. Impact assessment
    main = f"""
<section class="section section--paper">
  <div class="container">
    <div class="offerings">
      {offering("Impact evaluations", "Evaluations against the OECD-DAC criteria, using comparison groups where the design allows, and looking for unintended effects as well as intended ones. Examples: an impact evaluation of 23 implementing partners' projects for aBi (2021), and evaluations for Sida's Global Business Labs and for Caritas Switzerland.")}
      {offering("Jobs and income measurement", "Counting the jobs and income a programme creates, directly and further along the value chain. Example: a jobs tracer study and a job multiplier model for FCDO's Climate Smart Jobs programme (2025).")}
      {offering("Outcome studies at end-line", "Comparing end-line results with the baseline, by group and location. Shafiki Sabiiti worked as statistician on the end-line evaluation of 20 value-chain and financial-services projects funded by aBi Trust and aBi Finance (2024), and as data analyst on the Markets for Youth evaluation for GOAL and the Mastercard Foundation (2024&ndash;2025), which compared end-line results with baseline benchmarks.")}
      {offering("Impact and ESG measurement for investors", "Setting impact and ESG indicators for a lender or fund and tracking them across the portfolio. Sebyala Samuel built ESG-aligned credit scoring frameworks for the Segal Family Foundation.")}
    </div>
    <div class="note" data-reveal><strong>Methods.</strong> Household and enterprise surveys, comparison groups, key informant interviews, focus groups and case studies, chosen to fit the question and the budget. Where a comparison group is not possible, we say so and explain how the findings should be read.</div>
    <p class="table-caption" data-reveal>{EARLIER_NOTE}</p>
    {outputs("Evaluation designs and tools, impact assessment reports, jobs and income estimates, ESG and impact indicator frameworks, and short briefs for boards and funders.")}
  </div>
</section>"""
    service_page("impact-assessment",
        "Impact assessment asks what difference a programme or an investment made for the people and businesses it was meant to reach, compared with what would have happened without it.",
        "<p>It is separate from routine monitoring, and we offer it as a service in its own right.</p><p>Dr. Yusuf Kiwala leads this work. He trained in programme evaluation at the University of Oxford and with J-PAL at the University of Cape Town, and in MIS for M&amp;E at the University of East Anglia. His assignments include impact evaluations for aBi, Sida and Caritas Switzerland.</p>",
        "Principal Consultant, Impact Assessment. PhD, University of Pretoria; MBA and BCom (Finance), Makerere University.",
        main,
        "Impact evaluations, jobs and income measurement, outcome studies and impact and ESG measurement for investors, led by Dr. Yusuf Kiwala.")

    # ---------------------------------------------------------- 5. MIS
    main = f"""
<section class="section section--paper">
  <div class="container">
    <p class="note mt-0" data-reveal>{EARLIER_NOTE}</p>
    <div class="offerings mt-m">
      {offering("Information needs and system design", "User requirements, business processes and data structure. Team members designed the MIS and decision-support system for USAID's Water and Food Systems Activity, advised on the MIS for the Mastercard Foundation-supported SIYEP programme, and worked on the NAADS and NARO M&amp;E and MIS framework.")}
      {offering("Software development and integration", "Web and mobile applications, APIs, integration with ERP systems such as Microsoft Dynamics 365 Business Central and SAP, and moving databases to the cloud.")}
      {offering("Dashboards and reporting", "Power BI and R analysis, portfolio-at-risk dashboards, and dashboards that track programme performance.")}
      {offering("Data collection", "Mobile and digital data capture, with automatic checks, used across several implementing partners at once.")}
      {offering("Financial reporting tools", "An accounting and reporting tool for lower local governments and service units, and an assessment of the accounting software used by SACCOs.")}
      {offering("Credit and portfolio tools", "Arrears ageing, early-warning and recovery tracking; automated credit monitoring; a machine-learning credit-scoring application and a system for managing written-off loans.")}
      {offering("Manuals, training and support", "User manuals, standard operating procedures, training of trainers, and support after the system goes live.")}
    </div>
  </div>
</section>
<section class="section section--navy">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Results from team members' earlier work</span>
      <h2 class="display-3">What earlier systems achieved</h2>
    </div>
    <ol class="reasons">
      <li data-reveal><div><h3>Ministry of Finance</h3><p>A standalone financial reporting tool for lower local governments and service units, rolled out to 14 entities (Dr. Yusuf Kiwala, Team Leader, 2021).</p></div></li>
      <li data-reveal><div><h3>ERP extensions</h3><p>ERP extensions that cut manual data entry by more than half (Kazooba Simon).</p></div></li>
      <li data-reveal><div><h3>Iungo Capital</h3><p>Automated credit monitoring tools that halved reporting time (Sebyala Samuel).</p></div></li>
    </ol>
    <p class="note" data-reveal>{EARLIER_NOTE}</p>
  </div>
</section>"""
    service_page("management-information-systems",
        "When we design an MIS we start with the decisions managers have to make, then work back to the information those decisions need, where it comes from, how it is checked, and how it reaches the people who act on it.",
        "<p>Where needed, we also build the software and connect it to the systems the client already uses.</p><p>Kazooba Simon leads this work. He is an applications developer with more than ten years of experience building and supporting business systems. Dr. Yusuf Kiwala brings experience of MIS for monitoring and evaluation. Shafiki Sabiiti, as a systems analyst at a Ugandan lender, built a credit-scoring application and a system for managing written-off loans.</p>",
        "Head of Management Information Systems. BSc Computer Science, Makerere University; applications developer and solutions architect.",
        main,
        "Information needs and system design, software development and integration, dashboards, data collection and credit and portfolio tools, led by Kazooba Simon.")

    # ---------------------------------------------------------- 6. Market analysis
    main = f"""
<section class="section section--paper">
  <div class="container">
    <div class="offerings">
      {offering("Market and feasibility assessments", "Demand and supply, competition, pricing and the likely take-up of a product or project, usually with a financial model and business plan.")}
      {offering("Sector and value-chain studies", "Agriculture, commodity trade, agro-processing and microfinance, including the economics of inputs and commodity prices.")}
      {offering("Market segmentation", "Grouping customers by location, income and need, so that products and prices can be matched to each group.")}
      {offering("Customer and product research", "Surveys and interviews used to design savings, loan and insurance products for SACCOs and other financial institutions.")}
      {offering("How finance is priced and structured", "How lenders, guarantors and development finance institutions set terms. Sebyala Samuel has structured credit guarantee facilities with IFC, GuarantCo, ABSA, Old Mutual and Mastercard.")}
      {offering("Policy and trade studies", "Reviews of the rules and policies that shape a market, such as agricultural trade regulations across a region.")}
    </div>
    <div class="section-head mt-l" data-reveal>
      <span class="eyebrow">Examples from team members' earlier work</span>
    </div>
    {examples_table([
        ("USAID", "Data analysis and market segmentation to identify sanitation markets in Teso, Karamoja, Acholi, Lango, Sebei and Bugisu, and input to a market scorecard (statistician)", "Shafiki Sabiiti", "2024"),
        ("AESA East Africa", "Assessment of agricultural trade and market policies in IGAD member states (research associate)", "Shafiki Sabiiti", "2025"),
        ("Mercy Corps and IOM", "Market assessment, financial model and business plan for a proposed e-waste cooperative in Bidi Bidi settlement (Team Leader)", "Dickson Turyahabwe", "2025"),
        ("UCCFS (funded by WE EFFECT)", "Market research and new savings, loan and micro-insurance products for member SACCOs (Team Leader)", "Dickson Turyahabwe", "2015"),
    ])}
    <p class="table-caption" data-reveal>{EARLIER_NOTE}</p>
    {outputs("Market assessment reports, segmentation and demand estimates, financial models and business plans, product designs, and short briefs for management or the board.")}
  </div>
</section>"""
    service_page("market-analysis",
        "Market analysis earns its cost when it changes a decision about a product, a price, a new market or a partner.",
        "<p>We look at markets from the side of the investor and from the side of the SACCOs, cooperatives, farmers and households that finance and services are meant to reach.</p><p>Dickson Turyahabwe leads this work, with Shafiki Sabiiti on survey design, segmentation and analysis.</p>",
        "Principal Consultant, SMEs and Financial Inclusion. More than 20 years with SACCOs, MFIs, cooperatives and SMEs in Uganda, Rwanda and Tanzania.",
        main,
        "Market and feasibility assessments, sector and value-chain studies, segmentation, customer and product research and policy studies, led by Dickson Turyahabwe.")
