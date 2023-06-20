from model.contactData import ContactData


def test_modify_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(ContactData(nickname="Test"))
    app.contact.modify_first_contact(ContactData(nickname="nick name"))


def test_modify_contact_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(ContactData(homepage="Test"))
    app.contact.modify_first_contact(ContactData(homepage="www.homepage.com"))


def test_modify_contact_aday(app):
    if app.contact.count() == 0:
        app.contact.create(ContactData(aday="10"))
    app.contact.modify_first_contact(ContactData(aday="11"))


def test_modify_contact_amonth(app):
    if app.contact.count() == 0:
        app.contact.create(ContactData(amonth="October"))
    app.contact.modify_first_contact(ContactData(amonth="November"))


def test_modify_contact_ayear(app):
    if app.contact.count() == 0:
        app.contact.create(ContactData(ayear="2010"))
    app.contact.modify_first_contact(ContactData(ayear="2011"))
