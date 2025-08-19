import os
from streamlit.testing.v1 import AppTest

def test_app_title():
    """The app title is displayed correctly"""
    at = AppTest.from_file("app/main.py").run()

    app_env = at.secrets.get("APP_ENV", os.getenv("APP_ENV", "dev"))
    color = {"prod": "red", "qa": "orange"}.get(app_env, "green")

    assert at.title[0].value == f":{color}[{app_env.upper()} Environment]"
