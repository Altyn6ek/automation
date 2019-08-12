from fixture.application import Application
import pytest


@pytest.fixture(scope="session")
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()
