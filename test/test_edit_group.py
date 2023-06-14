from model.group import Group
import time


def test_edit_first_group(app):
    time.sleep(1)
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="text", header="teext", footer="teeext"))
    app.session.logout()
