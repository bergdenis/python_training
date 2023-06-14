# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app):
    time.sleep(1)
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test", header="teest", footer="teeest"))
    app.session.logout()


def test_add_empty_group(app):
    time.sleep(1)
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
