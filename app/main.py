import os
import streamlit as st

app_env = os.getenv("APP_ENV", "dev")

#TODO: Change color based on environment
st.title(f"Current environment: {app_env}")