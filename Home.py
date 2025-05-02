import streamlit as st

# Set the page configuration (affects all pages)
st.set_page_config(
    page_title="Finance Automation App",
    page_icon="🪙",
    layout="wide"
)

# Optional home display (if user doesn’t click any page)
st.markdown("# Welcome to the Finance Automation App")
st.markdown("Use the sidebar to navigate between pages like Login or Project Dashboard.")

