# -*- coding: utf-8 -*-
from model.contactData import ContactData
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxlen):
    symbols = string.digits + "()-"
    digits = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    if random.choice([True, False]):
        digits = "+" + digits
    return digits


testdata = [
    ContactData(firstname=random_string("firstname", 10) if random.choice([True, False]) else "",
                lastname=random_string("lastname", 10) if random.choice([True, False]) else "",
                address=random_string("address", 20) if random.choice([True, False]) else "",
                email=random_string("email", 10) + "@mail.com" if random.choice([True, False]) else "",
                email2=random_string("email2", 10) + "@mail.com" if random.choice([True, False]) else "",
                email3=random_string("email3", 10) + "@mail.com" if random.choice([True, False]) else "",
                home_number=random_digits(9) if random.choice([True, False]) else "",
                mobile_number=random_digits(9) if random.choice([True, False]) else "",
                work_number=random_digits(9) if random.choice([True, False]) else "",
                secondary_number=random_digits(9) if random.choice([True, False]) else "")
    for i in range(7)
]


@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)
