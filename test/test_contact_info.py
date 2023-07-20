import re
from model.contactData import ContactData


def test_contact_info_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactData(firstname="Test"))
    contacts_from_db = db.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()
    assert sorted(contacts_from_db, key=ContactData.id_or_max) == sorted(contacts_from_home_page, key=ContactData.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_number, contact.mobile_number, contact.work_number, contact.secondary_number]))))
