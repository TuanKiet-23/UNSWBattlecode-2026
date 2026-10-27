"""BigHero Streamlit showcase.

Deploy from the existing GitHub repo: TuanKiet-23/UNSWBattlecode-2026.
Place this file at the REPOSITORY ROOT and rename it to app.py.
Keep the existing docs/index.html (including embedded silent replay video).
"""

from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
WEBSITE = ROOT / "docs" / "index.html"
GITHUB = "https://github.com/TuanKiet-23/UNSWBattlecode-2026"

st.set_page_config(
    page_title="BigHero | UNSW Battlecode 2026",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Let the existing custom website occupy the full Streamlit viewport.
st.markdown(
    """
    <style>
      .block-container {
        padding: 0 !important;
        max-width: 100% !important;
      }
      [data-testid="stAppViewContainer"] { background: #f1f2ea; }
      [data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"],
      footer, #MainMenu { display: none !important; }
      [data-testid="stVerticalBlock"], [data-testid="stElementContainer"] {
        gap: 0 !important;
      }
      iframe { border: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

if not WEBSITE.is_file():
    st.error("Cannot find docs/index.html. Keep your current BigHero website file inside docs/.")
    st.link_button("View the original GitHub repository", GITHUB)
else:
    # The official Streamlit iframe supports HTML, JS, and dynamic content sizing.
    # This embeds the actual BigHero website, not a screenshot or a mockup.
    st.iframe(
        WEBSITE,
        width="stretch",
        height="content",
        alt="BigHero interactive strategy-bot project portfolio with an original silent example match video",
    )
