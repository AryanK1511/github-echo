import pytest


@pytest.fixture(autouse=True)
def set_dummy_env_vars(monkeypatch):
    monkeypatch.setenv('google_gemini_api_key', 'Sample')
    monkeypatch.setenv('github_api_token', 'Sample')
    monkeypatch.setenv('groq_api_key', 'Sample')
