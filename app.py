import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="異界陣ジェネレーター",
    page_icon="🜁",
    layout="wide",
)

html_path = Path(__file__).parent / "index.html"

if not html_path.exists():
    st.error("index.html が見つかりません。app.py と同じフォルダに置いてください。")
    st.stop()

html = html_path.read_text(encoding="utf-8")

components.html(
    html,
    height=1800,
    scrolling=True,
)