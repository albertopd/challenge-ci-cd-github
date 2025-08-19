import os
import streamlit as st
from streamlit.testing.v1 import AppTest

app_env = os.getenv("APP_ENV", "dev")

def test_app_title(monkeypatch):
    """The app title is displayed correctly"""

    # Fake secrets so Streamlit doesn't fail
    monkeypatch.setattr(st, "secrets", {"APP_ENV": app_env})

    at = AppTest.from_file("app/main.py").run()

    color = {"prod": "red", "qa": "orange"}.get(app_env, "green")

    assert at.title[0].value == f":{color}[{app_env.upper()} Environment]"
