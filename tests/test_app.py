import os
from streamlit.testing.v1 import AppTest

app_env = os.getenv("APP_ENV", "dev")

def test_app_title():
    """The app title is displayed correctly"""
    at = AppTest.from_file("app/main.py").run()
    assert at.title[0].value == f"Current environment: {app_env}"
