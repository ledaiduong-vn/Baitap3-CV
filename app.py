from __future__ import annotations

import io
from datetime import datetime

import streamlit as st

REPORTLAB_AVAILABLE = True
REPORTLAB_IMPORT_ERROR = ""
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.pdfgen import canvas
except ImportError as exc:
    REPORTLAB_AVAILABLE = False
    REPORTLAB_IMPORT_ERROR = str(exc)


st.set_page_config(
    page_title="Le Dai Duong | Portfolio & CV Builder",
    page_icon="⚡",
    layout="wide",
)


PROFILE = {
    "name": "LE DAI DUONG",
    "title": "Plant Manager | Renewable Energy Operations",
    "tagline": (
        "11+ years in transmission energy, high-voltage substations, "
        "project management, and solar plant operations."
    ),
    "dob": "June 21, 1991",
    "location": "Lam Dong, Viet Nam",
    "phone": "+84 965 739786",
    "email": "ledaiduong686@gmail.com",
    "linkedin": "https://www.linkedin.com/in/le-dai-duong-3704b9169/",
}

STRENGTHS = [
    "Technical expertise: Over 11 years in energy systems O&M.",
    "People management: lead teams to meet performance goals.",
    "Problem-solving: strong decisions under pressure.",
    "Relationship management with authorities and power sector agencies.",
    "Safety awareness: strong HSE and industry compliance mindset.",
]

ACHIEVEMENTS = [
    "Participated in managing a 30MW solar plant project to successful operation at FIT 1 tariff.",
    "Managed O&M for 39MWp and 50MWp solar plants, consistently meeting annual output targets (>55 GWh and >80 GWh) without significant incidents.",
    "Maintained stable career growth and operational leadership progression.",
]

SKILLS = [
    "O&M for automatic electrical systems, solar systems, and substations",
    "Fault identification, diagnosis, and troubleshooting",
    "Knowledge of Vietnam electricity regulations",
    "Communication and fast learning ability",
    "Microsoft Office, MS Project, Power BI, basic Python, AutoCAD 2D/3D",
    "Driver's license",
]

EXPERIENCE = [
    {
        "role": "Plant Manager",
        "period": "12/2024 - Now",
        "company": "Vinh Hao 6 (50MWp Solar Plant) - Leader Energy Group",
        "details": [
            "Manage all O&M activities",
            "Monitor daily power generation performance",
            "Resolve technical incidents",
            "Plan maintenance and budget",
            "Ensure HSE, reports, permits, and licenses compliance",
        ],
    },
    {
        "role": "Plant Manager & Head of Substation",
        "period": "06/2019 - 10/2024",
        "company": "Tuy Phong 39MWp Solar Plant - Power Plus Viet Nam",
        "details": [
            "Monitored equipment and generation efficiency",
            "Supervised staff, budgets, schedules, and safety compliance",
            "Maintained stakeholder relationships",
        ],
    },
    {
        "role": "Project Manager",
        "period": "10/2018 - 06/2019",
        "company": "Tuy Phong 39MWp Solar Plant Project - Power Plus Viet Nam",
        "details": [
            "Built project plans, schedules, budgets, and performance goals",
            "Oversaw design and construction for renewable facilities",
            "Coordinated project teams for on-time completion",
        ],
    },
    {
        "role": "Technical Staff",
        "period": "07/2017 - 10/2018",
        "company": "Technical Department - Power Transmission No.3",
        "details": [
            "Handled substation operations and incidents",
            "Developed standard O&M processes",
        ],
    },
    {
        "role": "O&M Engineer",
        "period": "09/2014 - 07/2017",
        "company": "Vinh Tan 500kV, Ham Tan 220kV, Thap Cham 220kV - Power Transmission No.3",
        "details": [
            "Supervised substation construction and installation",
            "Operated and maintained substations, resolved incidents",
        ],
    },
]

EDUCATION_CERTS = [
    "University of Technical Education Ho Chi Minh City - Bachelor of Electric Automation",
    "EVNNLDC - Certificate of Operation: Power Factory & Substation",
    "PACE - Action Plan & Performance Report",
    "HCM City Electric Power College - Medium voltage cable installation techniques",
    "Fulbright University - Capacity building in natural resource management",
]

LANGUAGE = {
    "English": "Working proficiency",
    "Speaking": "Moderate",
    "Listening": "Fair",
    "Writing": "Fair",
    "Reading": "Good",
}


def apply_custom_style() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background-image:
                linear-gradient(rgba(10, 25, 47, 0.82), rgba(8, 18, 35, 0.88)),
                url("https://images.unsplash.com/photo-1466611653911-95081537e5b7?auto=format&fit=crop&w=1600&q=80");
            background-size: cover;
            background-attachment: fixed;
            color: #f5f7fb;
        }
        section[data-testid="stSidebar"] {
            background: rgba(7, 17, 33, 0.85);
            border-right: 1px solid rgba(255, 255, 255, 0.15);
        }
        .glass {
            background: rgba(12, 28, 52, 0.72);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 14px;
            padding: 1rem 1.2rem;
            margin-bottom: 1rem;
            backdrop-filter: blur(6px);
        }
        .hero {
            font-size: 2.05rem;
            font-weight: 700;
            margin-bottom: 0.1rem;
        }
        .subhero {
            font-size: 1.1rem;
            color: #c9d8f3;
            margin-bottom: 0.8rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def draw_pdf_header(c: canvas.Canvas, template: str) -> None:
    if template == "Executive Navy":
        primary = colors.HexColor("#0B1F3A")
        accent = colors.HexColor("#D9A441")
    elif template == "Clean Blue":
        primary = colors.HexColor("#0A3D62")
        accent = colors.HexColor("#3C91E6")
    else:
        primary = colors.HexColor("#1F4D3D")
        accent = colors.HexColor("#7FB069")

    c.setFillColor(primary)
    c.rect(0, A4[1] - 4.5 * cm, A4[0], 4.5 * cm, fill=1, stroke=0)
    c.setFillColor(accent)
    c.rect(0, A4[1] - 4.8 * cm, A4[0], 0.3 * cm, fill=1, stroke=0)

    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(2 * cm, A4[1] - 2.1 * cm, PROFILE["name"])
    c.setFont("Helvetica", 12)
    c.drawString(2 * cm, A4[1] - 2.9 * cm, PROFILE["title"])
    c.setFont("Helvetica", 10)
    c.drawString(
        2 * cm,
        A4[1] - 3.6 * cm,
        f"{PROFILE['phone']}  |  {PROFILE['email']}  |  {PROFILE['location']}",
    )


def write_wrapped(c: canvas.Canvas, text: str, x: float, y: float, max_width: float, leading: float = 13) -> float:
    words = text.split()
    line = ""
    for word in words:
        test = f"{line} {word}".strip()
        if c.stringWidth(test, "Helvetica", 10) <= max_width:
            line = test
        else:
            c.drawString(x, y, line)
            y -= leading
            line = word
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def build_cv_pdf(template: str) -> bytes:
    if not REPORTLAB_AVAILABLE:
        raise RuntimeError("reportlab is not installed")

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    draw_pdf_header(c, template)

    y = A4[1] - 5.6 * cm
    c.setFillColor(colors.black)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "PROFESSIONAL SUMMARY")
    y -= 0.55 * cm
    c.setFont("Helvetica", 10)
    y = write_wrapped(c, PROFILE["tagline"], 2 * cm, y, A4[0] - 4 * cm)
    y -= 0.2 * cm

    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "CORE STRENGTHS")
    y -= 0.55 * cm
    c.setFont("Helvetica", 10)
    for item in STRENGTHS:
        y = write_wrapped(c, f"- {item}", 2.3 * cm, y, A4[0] - 4.3 * cm)
        if y < 4 * cm:
            c.showPage()
            y = A4[1] - 2.2 * cm
            c.setFont("Helvetica", 10)

    y -= 0.2 * cm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "EMPLOYMENT HISTORY")
    y -= 0.55 * cm

    for exp in EXPERIENCE:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(2 * cm, y, f"{exp['role']} ({exp['period']})")
        y -= 0.45 * cm
        c.setFont("Helvetica-Oblique", 10)
        y = write_wrapped(c, exp["company"], 2 * cm, y, A4[0] - 4 * cm)
        c.setFont("Helvetica", 10)
        for detail in exp["details"]:
            y = write_wrapped(c, f"• {detail}", 2.3 * cm, y, A4[0] - 4.3 * cm)
        y -= 0.2 * cm
        if y < 3.5 * cm:
            c.showPage()
            y = A4[1] - 2.2 * cm

    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, y, "EDUCATION & CERTIFICATES")
    y -= 0.55 * cm
    c.setFont("Helvetica", 10)
    for item in EDUCATION_CERTS:
        y = write_wrapped(c, f"- {item}", 2.3 * cm, y, A4[0] - 4.3 * cm)
        if y < 2.5 * cm:
            c.showPage()
            y = A4[1] - 2.2 * cm

    c.setFont("Helvetica", 9)
    c.setFillColor(colors.grey)
    c.drawRightString(A4[0] - 1.5 * cm, 1.2 * cm, f"Generated by Streamlit CV Builder - {datetime.now():%d/%m/%Y}")

    c.save()
    buffer.seek(0)
    return buffer.getvalue()


def intro_page() -> None:
    st.markdown(f"<div class='hero'>{PROFILE['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subhero'>{PROFILE['title']}</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='glass'><b>Professional value:</b> {PROFILE['tagline']}</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.15, 1])
    with col1:
        st.markdown("<div class='glass'><h4>Key Strengths</h4></div>", unsafe_allow_html=True)
        for item in STRENGTHS:
            st.markdown(f"- {item}")
        st.markdown("<div class='glass'><h4>Major Achievements</h4></div>", unsafe_allow_html=True)
        for item in ACHIEVEMENTS:
            st.markdown(f"- {item}")

    with col2:
        st.markdown("<div class='glass'><h4>Personal Information</h4></div>", unsafe_allow_html=True)
        st.write(f"**Date of birth:** {PROFILE['dob']}")
        st.write(f"**Location:** {PROFILE['location']}")
        st.write(f"**Phone:** {PROFILE['phone']}")
        st.write(f"**Email:** {PROFILE['email']}")
        st.write(f"**LinkedIn:** {PROFILE['linkedin']}")

        st.markdown("<div class='glass'><h4>Tools & Skills</h4></div>", unsafe_allow_html=True)
        for s in SKILLS:
            st.markdown(f"- {s}")


def cv_builder_page() -> None:
    st.subheader("Create Your CV in Multiple Professional Templates")
    if not REPORTLAB_AVAILABLE:
        st.error(
            "PDF export is unavailable because `reportlab` is missing in your environment.\n\n"
            "Please run: `pip install reportlab` or `pip install -r requirements.txt`"
        )
        if REPORTLAB_IMPORT_ERROR:
            st.caption(f"Import error: {REPORTLAB_IMPORT_ERROR}")
        return

    template = st.selectbox(
        "Select CV style",
        ["Executive Navy", "Clean Blue", "Energy Green"],
        index=0,
    )

    st.info(
        "CV content is generated based on your provided profile and optimized to highlight "
        "leadership, operational reliability, and renewable energy expertise."
    )

    with st.expander("Preview core CV content", expanded=True):
        st.markdown(f"### {PROFILE['name']}")
        st.markdown(PROFILE["tagline"])
        st.markdown("**Core strengths**")
        for item in STRENGTHS:
            st.markdown(f"- {item}")

    pdf_bytes = build_cv_pdf(template)
    st.download_button(
        label=f"Download CV PDF ({template})",
        data=pdf_bytes,
        file_name=f"Le_Dai_Duong_CV_{template.replace(' ', '_')}.pdf",
        mime="application/pdf",
        use_container_width=True,
    )


def main() -> None:
    apply_custom_style()
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Choose section",
        ["Personal Portfolio", "CV Builder (PDF Export)"],
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Highlighted Expertise")
    st.sidebar.markdown("- Solar plant operations")
    st.sidebar.markdown("- High-voltage substations")
    st.sidebar.markdown("- O&M leadership and HSE compliance")

    if page == "Personal Portfolio":
        intro_page()
    else:
        cv_builder_page()


if __name__ == "__main__":
    main()
