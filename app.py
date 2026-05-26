import streamlit as st
import requests
import time

st.set_page_config(
    page_title="ClutchHire AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    background-color: #050A05 !important;
    color: #D4E8D4 !important;
}
#MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none; }

.block-container {
    padding: 2.5rem 2.5rem 3rem 2.5rem !important;
    max-width: 1400px !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #030703 !important;
    border-right: 1px solid #0D2010 !important;
}
[data-testid="stSidebar"] .block-container {
    padding: 1.75rem 1.25rem !important;
}

/* Text area */
.stTextArea textarea {
    background: #070F07 !important;
    border: 1px solid #0F2A0F !important;
    border-radius: 10px !important;
    color: #D4E8D4 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    padding: 14px !important;
}
.stTextArea textarea:focus {
    border-color: #22C55E !important;
    box-shadow: 0 0 0 3px rgba(34,197,94,0.1) !important;
    outline: none !important;
}
.stTextArea textarea::placeholder { color: #1E4020 !important; }
.stTextArea label {
    font-family: 'Syne', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: #2A5C2A !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: #070F07 !important;
    border: 1px dashed #0F2A0F !important;
    border-radius: 10px !important;
    padding: 1.25rem !important;
}
[data-testid="stFileUploader"]:hover { border-color: #22C55E !important; }
[data-testid="stFileUploader"] label {
    font-family: 'Syne', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: #2A5C2A !important;
}
[data-testid="stFileUploader"] section { background: transparent !important; border: none !important; }
[data-testid="stFileUploader"] section small { color: #1E4020 !important; }
[data-testid="stFileUploader"] section button {
    background: #0A1A0A !important;
    border: 1px solid #0F2A0F !important;
    color: #4A9C5A !important;
    border-radius: 6px !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #16A34A 0%, #22C55E 100%) !important;
    color: #000000 !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 13px !important;
    font-weight: 800 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    height: 52px !important;
    width: 100% !important;
    box-shadow: 0 4px 24px rgba(34,197,94,0.3) !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 32px rgba(34,197,94,0.45) !important;
}

/* Metric widget */
[data-testid="metric-container"] {
    background: #070F07 !important;
    border: 1px solid #0F2A0F !important;
    border-radius: 10px !important;
    padding: 14px 18px !important;
}
[data-testid="metric-container"] label {
    color: #2A5C2A !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 10px !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 26px !important;
    font-weight: 700 !important;
}

/* Divider */
hr { border-color: #0D2010 !important; margin: 1rem 0 !important; }

/* Spinner */
.stSpinner > div { border-top-color: #22C55E !important; }

/* Info / warning / error */
[data-testid="stInfo"] {
    background: rgba(34,197,94,0.06) !important;
    border: 1px solid rgba(34,197,94,0.18) !important;
    color: #4ABA6A !important;
    border-radius: 10px !important;
}
[data-testid="stError"] {
    background: rgba(239,68,68,0.06) !important;
    border: 1px solid rgba(239,68,68,0.2) !important;
    border-radius: 10px !important;
}
[data-testid="stWarning"] {
    background: rgba(245,158,11,0.06) !important;
    border: 1px solid rgba(245,158,11,0.2) !important;
    border-radius: 10px !important;
}

/* Progress bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #16A34A, #22C55E) !important;
    border-radius: 4px !important;
}
.stProgress > div > div {
    background: #0D2010 !important;
    border-radius: 4px !important;
}

/* Expander */
[data-testid="stExpander"] {
    background: #070F07 !important;
    border: 1px solid #0F2A0F !important;
    border-radius: 10px !important;
}
[data-testid="stExpander"] summary {
    color: #FFFFFF !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
}

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #030703; }
::-webkit-scrollbar-thumb { background: #0F2A0F; border-radius: 2px; }
</style>
""", unsafe_allow_html=True)


# ── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="margin-bottom:1.75rem;">
        <div style="font-family:'Syne',sans-serif; font-size:21px; font-weight:800;
                    color:#FFFFFF; letter-spacing:-0.02em; line-height:1.15;">
            ClutchHire
        </div>
        <div style="font-family:'Syne',sans-serif; font-size:21px; font-weight:800;
                    color:#22C55E; letter-spacing:-0.02em; line-height:1.15; margin-bottom:5px;">
            AI
        </div>
        <div style="font-family:'DM Sans',sans-serif; font-size:10px; color:#1E4020;
                    letter-spacing:0.12em; text-transform:uppercase;">
            Talent Intelligence Platform
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="font-family:Syne,sans-serif;font-size:10px;font-weight:700;letter-spacing:0.14em;color:#1A3A1A;text-transform:uppercase;margin-bottom:10px;">Infrastructure</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#070F07;border:1px solid #0F2A0F;border-left:3px solid #22C55E;
                border-radius:8px;padding:12px 14px;margin-bottom:8px;">
        <div style="font-family:'DM Sans',sans-serif;font-size:10px;color:#1E4020;
                    text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Orchestration</div>
        <div style="font-family:'Syne',sans-serif;font-size:13px;font-weight:700;
                    color:#FFFFFF;margin-bottom:5px;">ClutchHire DeepSystem</div>
        <div style="display:flex;align-items:center;gap:5px;">
            <span style="width:6px;height:6px;background:#22C55E;border-radius:50%;
                         display:inline-block;box-shadow:0 0 6px #22C55E;"></span>
            <span style="font-family:'DM Sans',sans-serif;font-size:11px;color:#22C55E;">Online</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#070F07;border:1px solid #0F2A0F;border-left:3px solid #4ADE80;
                border-radius:8px;padding:12px 14px;margin-bottom:20px;">
        <div style="font-family:'DM Sans',sans-serif;font-size:10px;color:#1E4020;
                    text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Inference Engine</div>
        <div style="font-family:'Syne',sans-serif;font-size:13px;font-weight:700;
                    color:#FFFFFF;margin-bottom:4px;">DeepSeek Thinking</div>
        <div style="font-family:'DM Sans',sans-serif;font-size:11px;color:#2A5C2A;">DeepSeek V3.2 TEE</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="font-family:Syne,sans-serif;font-size:10px;font-weight:700;letter-spacing:0.14em;color:#1A3A1A;text-transform:uppercase;margin-bottom:10px;">Pipeline</div>', unsafe_allow_html=True)

    for num, name, desc in [
        ("01", "Parser",   "Extracts structured data from raw text"),
        ("02", "Scorer",   "Computes technical alignment score"),
        ("03", "Explainer","Generates recruiter-grade insights"),
    ]:
        st.markdown(f"""
        <div style="display:flex;gap:10px;align-items:flex-start;
                    padding-bottom:12px;margin-bottom:12px;border-bottom:1px solid #0A1E0A;">
            <div style="font-family:'Syne',sans-serif;font-size:10px;font-weight:700;
                        color:#22C55E;min-width:20px;padding-top:1px;">{num}</div>
            <div>
                <div style="font-family:'Syne',sans-serif;font-size:12px;font-weight:600;
                            color:#FFFFFF;margin-bottom:2px;">{name}</div>
                <div style="font-family:'DM Sans',sans-serif;font-size:11px;
                            color:#1E4020;line-height:1.4;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── HEADER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-bottom:2rem;">
    <div style="display:flex;align-items:baseline;gap:12px;margin-bottom:6px;">
        <span style="font-family:'Syne',sans-serif;font-size:38px;font-weight:800;
                     color:#FFFFFF;letter-spacing:-0.03em;line-height:1;">Talent Match</span>
        <span style="font-family:'Syne',sans-serif;font-size:38px;font-weight:800;
                     color:#22C55E;letter-spacing:-0.03em;line-height:1;">Engine</span>
    </div>
    <div style="font-family:'DM Sans',sans-serif;font-size:13px;color:#2A5C2A;letter-spacing:0.01em;">
        <span style="color:#22C55E;font-weight:500;">Multi-agent AI pipeline</span>
        <span style="color:#0F2A0F;"> &nbsp;·&nbsp; </span>
        <span style="color:#FFFFFF;">Parse</span>
        <span style="color:#22C55E;"> → </span>
        <span style="color:#FFFFFF;">Score</span>
        <span style="color:#22C55E;"> → </span>
        <span style="color:#FFFFFF;">Explain</span>
        <span style="color:#0F2A0F;"> &nbsp;·&nbsp; </span>
        <span style="color:#2A5C2A;">Powered by </span>
        <span style="color:#22C55E;">ClutchHire DeepSystem</span>
    </div>
</div>
""", unsafe_allow_html=True)

left_col, right_col = st.columns([5, 7], gap="large")


# ── LEFT PANEL ───────────────────────────────────────────────────────────────
with left_col:
    st.markdown('<div style="font-family:Syne,sans-serif;font-size:11px;font-weight:700;letter-spacing:0.12em;color:#1E4020;text-transform:uppercase;margin-bottom:14px;">Input Configuration</div>', unsafe_allow_html=True)

    jd_input = st.text_area(
        "JOB DESCRIPTION",
        placeholder="Paste the full job description — role, required skills, responsibilities...",
        height=230,
        key="jd_field"
    )

    st.markdown("<div style='height:0.75rem'></div>", unsafe_allow_html=True)

    uploaded_files = st.file_uploader(
        "CANDIDATE RESUMES",
        type=["txt"],
        accept_multiple_files=True,
        help="Upload one .txt file per candidate.",
        key="resume_uploader"
    )

    if uploaded_files:
        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        c1.metric("Resumes", len(uploaded_files))
        c2.metric("Agents", "3")
        c3.metric("Est. Time", f"~{len(uploaded_files)*2}s")

    st.markdown("<div style='height:0.75rem'></div>", unsafe_allow_html=True)
    trigger = st.button("⚡  Execute Match Pipeline", use_container_width=True)


# ── RIGHT PANEL ──────────────────────────────────────────────────────────────
with right_col:
    st.markdown('<div style="font-family:Syne,sans-serif;font-size:11px;font-weight:700;letter-spacing:0.12em;color:#1E4020;text-transform:uppercase;margin-bottom:14px;">Evaluation Insights</div>', unsafe_allow_html=True)

    if not trigger:
        st.info("⚡  System standby — configure inputs and execute the pipeline to see results here.")

    if trigger:
        if not jd_input.strip() or not uploaded_files:
            st.error("⚠️  Please provide both a job description and at least one resume file.")
        else:
            payload_files = [("resumes", (f.name, f.getvalue(), "text/plain")) for f in uploaded_files]
            payload_data  = {"jd": jd_input}

            with st.spinner("Running multi-agent pipeline..."):
                t_start = time.time()
                try:
                    resp = requests.post(
                        "http://127.0.0.1:8000/analyze",
                        data=payload_data,
                        files=payload_files,
                        timeout=120
                    )
                    elapsed = round(time.time() - t_start, 1)

                    if resp.status_code == 200:
                        data       = resp.json()
                        candidates = data.get("candidates", [])

                        if candidates:
                            top = candidates[0]

                            # ── Summary metrics ──
                            m1, m2, m3 = st.columns(3)
                            m1.metric("Evaluated",  f"{len(candidates)} profiles")
                            m2.metric("Top Score",  f"{top['score']}%")
                            m3.metric("Runtime",    f"{elapsed}s")

                            st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
                            st.divider()

                            # ── Candidate cards ──
                            for i, c in enumerate(candidates):
                                score = c["score"]
                                rank  = i + 1

                                if score >= 80:
                                    bar_color   = "#22C55E"
                                    tier        = "STRONG MATCH"
                                    tier_color  = "#22C55E"
                                elif score >= 55:
                                    bar_color   = "#F59E0B"
                                    tier        = "PARTIAL MATCH"
                                    tier_color  = "#F59E0B"
                                else:
                                    bar_color   = "#EF4444"
                                    tier        = "LOW MATCH"
                                    tier_color  = "#EF4444"

                                crown = "👑 " if rank == 1 else f"#{rank} "

                                # Card header
                                st.markdown(f"""
                                <div style="background:#070F07;border:1px solid #0F2A0F;
                                            border-top:2px solid {bar_color};
                                            border-radius:12px;padding:18px 20px 6px 20px;
                                            margin-top:10px;">
                                    <div style="display:flex;justify-content:space-between;
                                                align-items:flex-start;margin-bottom:6px;">
                                        <div>
                                            <div style="font-family:'Syne',sans-serif;font-size:17px;
                                                        font-weight:700;color:#FFFFFF;margin-bottom:3px;">
                                                {crown}{c['name']}
                                            </div>
                                            <div style="font-family:'DM Sans',sans-serif;font-size:10px;
                                                        font-weight:700;letter-spacing:0.12em;
                                                        color:{tier_color};text-transform:uppercase;">
                                                {tier}
                                            </div>
                                        </div>
                                        <div style="text-align:right;">
                                            <div style="font-family:'Syne',sans-serif;font-size:28px;
                                                        font-weight:800;color:{bar_color};line-height:1;">
                                                {score}<span style="font-size:14px;color:{bar_color};
                                                opacity:0.6;">%</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)

                                # Score bar — native Streamlit progress
                                st.progress(score / 100)

                                # Tags row
                                tags_html = "".join([
                                    f'<span style="background:#0A1A0A;border:1px solid #0F2A0F;'
                                    f'color:#4ADE80;padding:3px 10px;border-radius:20px;'
                                    f'font-size:11px;font-family:DM Sans,sans-serif;'
                                    f'display:inline-block;margin:2px 3px 2px 0;">{tag}</span>'
                                    for tag in c["match_tags"]
                                ])
                                st.markdown(
                                    f'<div style="padding:8px 0 4px 0;">{tags_html}</div>',
                                    unsafe_allow_html=True
                                )

                                # Explanation in expander
                                with st.expander("View recruiter analysis"):
                                    st.markdown(
                                        f'<p style="font-family:DM Sans,sans-serif;font-size:14px;'
                                        f'color:#A0C8A0;line-height:1.7;margin:0;">'
                                        f'{c["explanation"]}</p>',
                                        unsafe_allow_html=True
                                    )

                                st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

                        else:
                            st.warning("No candidates were returned. Check that your resume files contain readable text.")

                    else:
                        try:
                            detail = resp.json().get("detail", resp.text)
                        except Exception:
                            detail = resp.text
                        st.error(f"Backend Error {resp.status_code}: {detail}")

                except requests.exceptions.ConnectionError:
                    st.error("Cannot reach backend at port 8000. Make sure `python main.py` is running in a separate terminal.")
                except Exception as e:
                    st.error(f"Unexpected error: {str(e)}")