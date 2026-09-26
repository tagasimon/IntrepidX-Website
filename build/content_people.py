from build import *

PEOPLE = [
    dict(name="Prof. Atukunda Gershom", initials="AG", home=True,
         role="Managing Director and Team Leader, Monitoring and Evaluation",
         quals="Associate Professor. PhD in Development Studies, Bishop Stuart University. MA in Ethics and Development Studies, Uganda Martyrs University. PGD in Monitoring and Evaluation, Uganda Management Institute",
         bio="Associate Professor at Bishop Stuart University, where he is Vice-Chancellor's Commissary and Director of Graduate Studies, Research and Innovations. He was Acting Vice-Chancellor (2023&ndash;2024) and Dean of the Faculty of Business, Economics and Governance (2016&ndash;2021). Since 2021 he has coordinated the university's part of RETI, a consortium project funded by the Mastercard Foundation, and he chaired the board of the EU-funded AgriScale project in 2023. He supervises PhD and master's research and chairs the Boards of Governors of several schools and colleges.",
         areas=["M&amp;E", "Research methods and statistics", "Organisational capacity assessment", "Governance", "Training"]),
    dict(name="Dr. Yusuf Kiwala", initials="YK", home=True,
         role="Principal Consultant, Impact Assessment",
         quals="PhD, University of Pretoria. MBA and BCom (Finance), Makerere University. Diploma in Management Information Systems",
         bio="Evaluation, MIS and public finance specialist with assignments going back to 2010. For aBi he led an impact evaluation of 23 implementing partners' projects and baselines for 20 projects (2021). He was Team Leader for the integrated MIS and decision-support system of USAID's Feed the Future Water and Food Systems Activity (2024), and in 2025 advised on a jobs tracer study for FCDO's Climate Smart Jobs programme and an integrated MIS for the Mastercard Foundation-supported SIYEP programme. He has also carried out evaluations for Sida, Caritas Switzerland and CSBAG. He has filed a Ugandan patent (UG/P/2024/000009) on using machine learning to predict outbreaks of foot-and-mouth disease.",
         areas=["Impact evaluation", "Jobs measurement", "Baselines", "M&amp;E systems", "MIS design", "Public finance assessment"]),
    dict(name="Sebyala Samuel, ACCA", initials="SS", home=True,
         role="Principal Consultant, Due Diligence and Credit Risk",
         quals="PhD student, Business Administration (Artificial Intelligence), Walsh College, USA. Master in Advanced Finance, IE Business School, Madrid. CFA Levels I and II passed. ACCA member since 2009",
         bio="Investment manager with more than 12 years' experience and over US$150 million of private-sector debt and equity transactions in 15 African and 2 European markets. Since 2023 he has been Distressed Debt Turnaround Strategist with the Uganda Bankers Association. For the Segal Family Foundation (2022&ndash;2023) he carried out credit due diligence on more than 45 social enterprises and impact funds. With PCP since 2021, he has managed a US$25 million SME credit portfolio with portfolio at risk below 3% and structured more than 12 credit guarantee facilities with IFC, GuarantCo, Old Mutual and Mastercard. He leads our due diligence, appraisal and valuation work and is Team Leader on the aBi Finance assignment.",
         areas=["Due diligence", "Credit risk", "Valuation", "Deal structuring", "Distressed debt"]),
    dict(name="Dickson Turyahabwe, CPA", initials="DT", home=True,
         role="Principal Consultant, SMEs and Financial Inclusion",
         quals="CPA, member of ICPAU and ICPAR. MBA, University of East London. BCom (Accounting), Makerere University. Certified Microfinance Trainer",
         bio="More than 20 years with SACCOs, MFIs, cooperatives and SMEs in Uganda, Rwanda and Tanzania. He was the first General Manager of Wazalendo SACCO, where portfolio at risk stayed below 2%, and earlier worked at UCSCU and on the USAID-funded WOCCU SACCONet project. He is Managing Partner of Dickson Associates and developed the SACCO financial diagnostic tool used under the IFAD-funded Rural Financial Services Programme. Recent clients include AMIR, Cordaid Rwanda, Mercy Corps and IOM, UNDP, Enabel and Oikocredit. He leads our post-investment support and market analysis work and is Delinquency Management Expert on the aBi Finance assignment.",
         areas=["SACCO and MFI strengthening", "SME support", "Market assessment", "Credit management", "Training"]),
    dict(name="Dean Niwarinda", initials="DN", home=True,
         role="Senior Investment Analyst, Company Secretary and Lead, Investment Analysis",
         quals="MBA (Finance) and BCom (Finance), Makerere University. CPA candidate, ICPAU",
         bio="Company Secretary of IntrepidX, with four years' experience in investment analysis, credit assessment, financial modelling and portfolio monitoring. Since 2023 he has worked in investment analysis with PCP across East and Southern Africa. As a junior consultant to the Segal Family Foundation (2024&ndash;2025) he supported credit due diligence and ESG-aligned credit scoring for social enterprises. He started his career in audit and assurance at BDO Uganda (2021&ndash;2022).",
         areas=[]),
    dict(name="Kazooba Simon", initials="KS", home=True,
         role="Head of Management Information Systems",
         quals="BSc Computer Science, Makerere University. Certificates in API design, Google Cloud database administration and Django",
         bio="Applications developer and solutions architect with more than ten years of experience designing, building and supporting business systems in manufacturing, hospitality and services. He is a Director of Elastic Technologies Ltd. At Mulwana Group he extended Microsoft Dynamics 365 Business Central and SAP through APIs and moved databases to Google Cloud. He uses Power BI and R for analysis and forecasting. He leads our MIS work and is MIS and Portfolio Analytics Specialist on the aBi Finance assignment.",
         areas=[]),
    dict(name="Shafiki Sabiiti", initials="SS", home=False,
         role="Statistician and Data Analyst",
         quals="BSc Statistics, Makerere University. MSc Statistics (in progress), Makerere University. Postgraduate Diploma in M&amp;E (in progress), Uganda Management Institute",
         bio="He has worked on surveys, M&amp;E and data since 2019. His work includes nationwide surveys for the Uganda Revenue Authority and the Ministry of Gender, Labour and Social Development; baselines and evaluations for aBi, GIZ and Mastercard Foundation-funded programmes, among them SIYEP and Enhancing Youth Employment in Coffee; and monitoring and market analysis for USAID-funded activities. As Systems Analyst at Real People Financial Services (since 2023) he built a machine-learning credit-scoring application and a system for managing written-off loans.",
         areas=[]),
    dict(name="Mutatinensi Dedan, CPA, ACCA, CTA", initials="MD", home=False,
         role="Tax and Regulatory Compliance Consultant",
         quals="CPA, ICPAU. ACCA. Certified Tax Advisor (CTA Level III), ICPAU. MBA. BCom, Makerere University",
         bio="More than ten years in tax advisory, audit and financial control. He has been Head of Tax and Business Advisory Services at Demo Consult Ltd since 2016, Senior Auditor with Peekay Steeve Associates CPA since 2019, and an external taxation management consultant with Alphabeta Project Consultants since 2023. He represents clients in URA audits, objections and disputes, carries out tax health checks, and advises on tax-efficient structures and double taxation agreements.",
         areas=[]),
    dict(name="Gilbert Flart, CPA", initials="GF", home=False,
         role="Financial Management and Controls Consultant",
         quals="CPA, ICPAU. MBA, Makerere University. BSc Accounting and Finance, Kyambogo University",
         bio="More than seven years in financial management, treasury, tax compliance and IFRS reporting. He is Finance Coordinator at Aga Khan Health Service, Uganda (with the organisation since 2022). Before that he was Financial Controller at Home Harvest (U) Ltd, where he put in an ERP and a costing system and handled grant reporting on projects supported by USAID Feed the Future and SNV.",
         areas=[]),
    dict(name="Solomon Ssekiranda, CPA, ACCA", initials="SS", home=False,
         role="Financial Analyst",
         quals="BCom (Upper Second Class Honours), Makerere University. ACCA member. CPA, full member of ICPAU",
         bio="Qualified accountant. In 2023 he completed the ACCA Strategic Professional examinations (Strategic Business Leader, Strategic Business Reporting, Advanced Financial Management and Advanced Performance Management). He supports our financial analysis and due diligence work.",
         areas=[]),
    dict(name="Tukamushaba Alvin", initials="TA", home=False,
         role="Associate Consultant",
         quals="BCom (Accounting), Makerere University. CPA candidate, ICPAU",
         bio="Accountant with experience in audit, donor-funded project finance and field surveys. He started as an audit assistant with Kabagambe and Associates (2021&ndash;2022), then joined Okeba Uganda Ltd as an accountant and, from October 2022 to July 2023, was Projects Lead Assistant on the SNV-funded CRAFT project and the Young Africa Works programme (PSFU, Mastercard Foundation) in south-western Uganda. In 2024, through Demi's Consults Ltd, he assessed farmer organisations in Eastern, Northern and North-eastern Uganda for TechnoServe's HORTIMAP project. He was project accountant for FLAMA Health Uganda in the Acholi sub-region (2025&ndash;2026), and team leader for the baseline survey of SIYEP in West Nile (implemented by AFARD, funded by the Mastercard Foundation) through Mamza Consulting Ltd (2025&ndash;2026). Since 2023 he has also prepared accounts and filed PAYE, VAT and income tax returns for SMEs.",
         areas=[]),
    dict(name="Mutatina Seiz", initials="MS", home=False,
         role="Associate Consultant, M&amp;E and Risk Management",
         quals="BCom (Accounting), Makerere University. CPA candidate (Level 2), ICPAU. Income Tax Revenue Administration Training (ITRAT), URA",
         bio="Officer, Performance Management and Human Capital Development at the Uganda Revenue Authority since January 2026, after working there as a Performance Monitoring Officer. He was part of the core team that developed URA's Enterprise Risk Management Framework, and he trains departmental risk champions to spot and report risks early. He tracks departmental KPIs against strategic objectives, analyses workforce and productivity data, and prepares performance and risk reports and dashboards for management. Earlier he was a research assistant on the SCART project of the Ministry of Local Government (2022), collecting and checking field data and writing weekly monitoring reports, and an accounts assistant at International Hospital Kampala (2022&ndash;2023).",
         areas=[]),
]

# Staffing matrix from profile page 15: M = main area, S = supporting area, - = none
MATRIX_COLS = ["Due diligence, investment appraisal and valuation", "Post-investment support", "M&amp;E", "Impact assessment", "MIS", "Market analysis",
               "Credit and finance", "Tax and regulatory", "Financial controls", "Training"]
MATRIX = [
    ("Prof. Atukunda Gershom", "--M------M"),
    ("Dr. Yusuf Kiwala",       "S-MMMS--SS"),
    ("Sebyala Samuel",         "MM-SSSM---"),
    ("Dickson Turyahabwe",     "MMS-SMM-MM"),
    ("Dean Niwarinda",         "MS---SM-S-"),
    ("Kazooba Simon",          "----M----S"),
    ("Shafiki Sabiiti",        "--MSSSS--S"),
    ("Mutatinensi Dedan",      "S------MMS"),
    ("Gilbert Flart",          "-------SM-"),
    ("Solomon Ssekiranda",     "M-------S-"),
    ("Tukamushaba Alvin",      "-SS----SS-"),
    ("Mutatina Seiz",          "--S-----S-"),
]

def dot(c):
    if c == "M": return '<span class="dot dot--main" role="img" aria-label="Main area"></span>'
    if c == "S": return '<span class="dot dot--support" role="img" aria-label="Supporting area"></span>'
    return '<span class="dot dot--none" role="img" aria-label="Not an area of experience"></span>'

def team_page():
    root = ""
    profiles = ""
    for i, p in enumerate(PEOPLE, 1):
        areas = ""
        if p["areas"]:
            areas = '<ul class="profile__areas" aria-label="Areas of work">' + "".join(f"<li>{a}</li>" for a in p["areas"]) + "</ul>"
        profiles += f"""
    <article class="profile" id="{p['name'].split(',')[0].lower().replace('.', '').replace(' ', '-')}" data-reveal>
      <div class="profile__head">
        <h3>{p['name']}</h3>
        <p class="role">{p['role']}</p>
        <p class="profile__quals">{p['quals']}</p>
      </div>
      <div class="profile__body">
        <p>{p['bio']}</p>
        {areas}
      </div>
    </article>"""
    mhead = "<th>Team member</th>" + "".join(f"<th>{c}</th>" for c in MATRIX_COLS)
    mbody = "".join("<tr><td>" + n + "</td>" + "".join(f"<td>{dot(c)}</td>" for c in row) + "</tr>" for n, row in MATRIX)
    body = f"""
<main id="main">
{page_hero(root, "documents", "Two people reviewing documents at a table",
           [("index.html", "Home"), (None, "Team")], "Our people", "Our team",
           "Short profiles of the twelve people on the IntrepidX team. Full CVs are available on request.",
           '<div class="meta"><span>Languages: <strong>English, Luganda, Runyankore, Rukiga, Rutooro, Lusoga, Kiswahili, Kinyarwanda</strong></span></div>')}
<section class="section section--ivory">
  <div class="container">{profiles}
  </div>
</section>
<section class="section section--paper" id="staffing">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">How we staff assignments</span>
      <h2 class="display-2">Who works on what</h2>
      <p>Each assignment has a named Team Leader, who deals with the client and signs off every deliverable after an internal review. The rest of the team is chosen to fit the terms of reference.</p>
    </div>
    <div class="legend" data-reveal><span>{dot("M")} Main area</span><span>{dot("S")} Supporting area</span></div>
    <div class="table-wrap" data-reveal><table class="data-table matrix"><thead><tr>{mhead}</tr></thead><tbody>{mbody}</tbody></table></div>
    <p class="table-caption" data-reveal>Based on each person's CV and the firm's own assignments. Prof. Gershom's M&amp;E rating rests on his M&amp;E qualification and project leadership. Legal and technical due diligence and formal valuations use associate specialists.</p>
  </div>
</section>
{cta(root, "Request a CV or discuss an assignment", "Full CVs for everyone on this page are available on request. To discuss an assignment or request company documents for a tender, contact the Company Secretary, Dean Niwarinda, at dniwarinda@intrepidx.biz.")}
</main>
"""
    write("team.html", head(root, "team.html", "Our team",
                            "The twelve people on the IntrepidX team: evaluators, qualified accountants, an investment manager, a SACCO and microfinance practitioner, a statistician, a software developer and two associate consultants.")
          + header(root, "team.html") + body + footer(root))
