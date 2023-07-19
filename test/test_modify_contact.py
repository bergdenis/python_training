from model.contactData import ContactData
import random


def test_modify_contact_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactData(lastname="Test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    modified_contact = ContactData(lastname="new last name", id=contact.id)
    app.contact.modify_contact_by_id(contact.id, modified_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for i, c in enumerate(old_contacts):
        if c.id == contact.id:
            old_contacts[i] = modified_contact
            break
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactData.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactData.id_or_max)


# def test_modify_contact_firstname(app):
#     if app.contact.count() == 0:
#         app.contact.create(ContactData(firstname="Test"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = ContactData(firstname="first name")
#     contact.id = old_contacts[index].id
#     app.contact.modify_contact_by_index(index, contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[index].firstname = contact.firstname
#     assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)


# def test_modify_contact_nickname(app):
#     if app.contact.count() == 0:
#         app.contact.create(ContactData(nickname="Test"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = ContactData(nickname="nick name")
#     contact.id = old_contacts[index].id
#     app.contact.modify_contact_by_index(index, contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[index].nickname = contact.nickname
#     assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)


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

# def test_modify_contact_ayear(app):
#     if app.contact.count() == 0:
#         app.contact.create(ContactData(ayear="2010"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = ContactData(ayear="2011")
#     contact.id = old_contacts[index].id
#     app.contact.modify_contact_by_index(index, contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[index].ayear = contact.ayear
#     assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)
