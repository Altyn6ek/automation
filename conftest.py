from fixture.application import Application
import pytest


fixture = None


@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        baseUrl = request.config.getoption("--baseUrl")
        fixture = Application(browser=browser, baseUrl=baseUrl)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    yield fixture
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
