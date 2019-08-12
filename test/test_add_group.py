# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="group_name", header="group_header", footer="group_footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
