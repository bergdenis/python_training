import re
from model.contactData import ContactData


def test_contact_info_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactData(firstname="Test"))
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    sorted_contacts_home_page = sorted(contacts_from_home_page, key=ContactData.id_or_max)
    sorted_contacts_db = sorted(contacts_from_db, key=ContactData.id_or_max)
    for contact_home_page, contact_db in zip(sorted_contacts_home_page, sorted_contacts_db):
        assert contact_home_page.lastname == contact_db.lastname
        assert contact_home_page.firstname == contact_db.firstname
        assert contact_home_page.address == contact_db.address
        assert contact_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_db)
        assert contact_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)


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
