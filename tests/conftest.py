import os
import pytest


@pytest.fixture
def client(monkeypatch):
    db_path = os.path.abspath("tests/test.db")
    monkeypatch.setenv("SQLALCHEMY_DATABASE_URI", f"sqlite:///{db_path}")

    from app import init_app
    app = init_app()
    app.testing = True
    return app.test_client()
