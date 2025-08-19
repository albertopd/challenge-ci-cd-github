import streamlit as st

app_env = st.secrets.get("APP_ENV", "dev")

color = {"prod": "red", "qa": "orange"}.get(app_env, "green")

st.title(f":{color}[{app_env.upper()} Environment]")