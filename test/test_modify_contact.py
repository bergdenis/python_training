from model.contactData import ContactData


def test_modify_contact_nickname(app):
    app.contact.modify_first_contact(ContactData(nickname="nick name"))


def test_modify_contact_homepage(app):
    app.contact.modify_first_contact(ContactData(homepage="www.homepage.com"))


def test_modify_contact_aday(app):
    app.contact.modify_first_contact(ContactData(aday="11"))


def test_modify_contact_amonth(app):
    app.contact.modify_first_contact(ContactData(amonth="November"))


def test_modify_contact_ayear(app):
    app.contact.modify_first_contact(ContactData(ayear="2011"))
