# -*- coding: utf-8 -*-
from model.contactData import ContactData
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [ContactData(firstname="", lastname="", address="")] + [
    ContactData(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), address=random_string("address", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)


# home_number="111111", mobile_number="222222", work_number="333333",
#                           email="mail@mail.com", email2="mail2@mail.com", email3="mail3@mail.com", secondary_number="555555"