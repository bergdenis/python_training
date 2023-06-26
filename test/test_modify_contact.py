from model.contactData import ContactData


def test_modify_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(ContactData(nickname="Test"))
    old_contacts = app.contact.get_contact_list()
    contact = ContactData(nickname="nick name")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0].nickname = contact.nickname
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)


# def test_modify_contact_homepage(app):
#     if app.contact.count() == 0:
#         app.contact.create(ContactData(homepage="Test"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(ContactData(homepage="www.homepage.com"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_modify_contact_aday(app):
#     if app.contact.count() == 0:
#         app.contact.create(ContactData(aday="10"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(ContactData(aday="11"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_modify_contact_amonth(app):
#     if app.contact.count() == 0:
#         app.contact.create(ContactData(amonth="October"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(ContactData(amonth="November"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_modify_contact_ayear(app):
#     if app.contact.count() == 0:
#         app.contact.create(ContactData(ayear="2010"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(ContactData(ayear="2011"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
