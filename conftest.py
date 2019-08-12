from fixture.application import Application
import pytest


@pytest.fixture(scope="session")
# @pytest.fixture()
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()