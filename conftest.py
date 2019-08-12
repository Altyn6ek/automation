from fixture.application import Application
import pytest


# @pytest.fixture(scope='session')
@pytest.fixture(scope='session')
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()

# @pytest.fixture(scope='session')
# def app(request):
#     fixture = Application()
#     request.addfinalizer(fixture.destroy)
#     return fixture