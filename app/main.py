import os
import streamlit as st

env = os.getenv("ENVIRONMENT", "Development")

#TODO: Change color based on environment
st.success(f"Current environment: {env}")