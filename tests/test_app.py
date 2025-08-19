import os
import streamlit as st
from streamlit.testing.v1 import AppTest


def test_app_title(monkeypatch):
    """The app title is displayed correctly"""

    # Fake secrets so Streamlit doesn't fail
    monkeypatch.setattr(st, "secrets", {"APP_ENV": "dev"})

    at = AppTest.from_file("app/main.py").run()

    app_env = os.getenv("APP_ENV", "dev")
    color = {"prod": "red", "qa": "orange"}.get(app_env, "green")

    assert at.title[0].value == f":{color}[{app_env.upper()} Environment]"

