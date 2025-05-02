import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import time
from modules.full_hand_open import detect_hand_open

st.set_page_config(page_title="Smart Login", layout="wide" , initial_sidebar_state="collapsed")
if st.session_state.get("redirect_to_proj", False):
    st.session_state.redirect_to_proj = False
    st.switch_page("pages/2_DashBoard.py")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
# --- Custom CSS ---
st.markdown(
    """
    <style>
    @keyframes fadeInAnimation {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .main-container {
        animation: fadeInAnimation 2s ease;
    }
    body {
        background-image: url('https://wallpapercave.com/wp/wp1960402.jpg'); 
        background-size: cover;
        background-position: center center;
        background-attachment: fixed;  
        opacity: 1; 
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0); 
    }
    .big-title {
        font-size: 48px;
        font-weight: 800;
        text-align: left;
        margin-bottom: 10px;
        color: #f8f9fa;
    }
    .subtitle {
        font-size: 20px;
        text-align: left;
        margin-bottom: 30px;
        color: #adb5bd;
    }
    .vertical-line {
        border-left: 2px solid #ccc;
        height: 475px;
        margin: auto;
    }
    div.stButton > button {
        padding: 0.75em 1.5em;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.4s ease-in-out;
        border: 2px solid white;
    }
    div.stButton > button:nth-child(1) {
        background-color: #28a745;
        color: white;
    }
    div.stButton > button:nth-child(1):hover {
        background-color: #218838;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1), 0 0 10px #28a745;
        transform: scale(1.05);
        cursor: pointer;
    }
    div.stButton > button:nth-child(2) {
        background-color: #dc3545;
        color: white;
    }
    div.stButton > button:nth-child(2):hover {
        background-color: #c82333;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1), 0 0 10px #dc3545;
        transform: scale(1.05);
        cursor: pointer;
    }
    footer {
        position: fixed;
        bottom: 0;
        left: 27%;
        transform: translateX(-50%);
        width: auto;
        min-width: 300px;
        border-radius: 8px 8px 0 0;
        padding: 8px 16px;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
        text-align: center;
        z-index: 1000;
    }
    .stApp > div:first-child {
        padding-bottom: 100px !important;
    }
    </style>
    <div class="main-container">
    """,
    unsafe_allow_html=True
)

# --- Main Content ---
container = st.container()
with container:
    left_col, middle_col, right_col = st.columns([2, 0.05, 2])

# --- Left Column ---
with left_col:
    st.markdown('<div class="big-title">🔐 OpenCV Authentication Login Interface</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Welcome to my first intermediate Python project - Finance Automation to easily analyze Bank statements</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Before proceeding, please login with your preferred method: fun webcam or direct login 👇</div>', unsafe_allow_html=True)

    st.info("Choose your Login Method:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✌️ Login with cheese", use_container_width=True):
            st.session_state['show_webcam'] = True

    with col2:
        if st.button("🔓 Direct Click Login", use_container_width=True):
            with st.status("Logging in without gesture...", expanded=True) as status:
                time.sleep(1)
                status.update(label="Direct Login Successful ✅", state="complete")
                st.success("Logged in Directly!")
                st.warning("Please click STOP at top-right side of this page. Also refresh the page to do all process again!")
                time.sleep(1)
                st.session_state.logged_in = True
                st.session_state.redirect_to_proj = True
                st.rerun()


# --- Middle Column (Line) ---
with middle_col:
    st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)

# --- Right Column (Webcam + Captured Photo) ---
with right_col:
    st.markdown("### 📷 Webcam Feed and Hand Capture")

    if st.session_state.get('show_webcam', False):
        with st.spinner('Opening webcam... say cheeze 😁✌️'):
            time.sleep(1) 
            captured_frame = detect_hand_open()

        if captured_frame is not None:
            st.image(captured_frame, channels="BGR", caption="Captured Hand Open Gesture", use_column_width=True)
            st.success("Logged in Successfully!")
            time.sleep(1)
            st.session_state.logged_in = True
            st.session_state.show_webcam = False                 #SPECIAL LINE 
            st.session_state.redirect_to_proj = True
            st.rerun()

        else:
            st.warning("No gesture detected. Please try again.")
            st.stop()

# --- Fade-in Container Close ---
st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<footer>
    <hr style="border: 1px solid #bbb; margin-top: 50px; margin-bottom: 10px;">
    <div style="text-align: center; padding-bottom: 20px;">
        <a href="https://www.linkedin.com/in/saharsh-sharma-a5712b287/" target="_blank" style="text-decoration: none; margin: 0 5px;">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30" style="vertical-align: middle;">
        </a>
        <a href="https://github.com/makankosappoh" target="_blank" style="text-decoration: none; margin: 0 5px;">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" width="30" style="vertical-align: middle;">
        </a>
        <a href="mailto:saharshsharma28@gmail.com" target="_blank" style="text-decoration: none; margin: 0 5px;">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="30" style="vertical-align: middle;">
        </a>
        <a href="https://www.instagram.com/saharsh_ssj/" target="_blank" style="text-decoration: none; margin: 0 5px;">
            <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="30" style="vertical-align: middle;">
        </a>
        <p style="font-size: 14px; color: #aaa; margin-bottom: -5px;">Connect with Me 😊</p>
    </div>
</footer>
""", unsafe_allow_html=True)
