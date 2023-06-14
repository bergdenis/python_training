import time


def test_delete_first_contact(app):
    time.sleep(1)
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
