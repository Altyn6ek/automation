from fixture.application import Application
import pytest


@pytest.fixture()
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()
