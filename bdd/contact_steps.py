from pytest_bdd import given, when, then, parsers
from model.contactData import ContactData
import random
import time


@given("a contact list", target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()


@given(parsers.parse("a contact with {firstname}, {lastname} and {email}"), target_fixture="new_contact")
def new_contact(firstname, lastname, email):
    return ContactData(firstname=firstname, lastname=lastname, email=email)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old contact list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)


@given("a non-empty contact list", target_fixture="non_empty_contact_list")
def non_empty_contact_list(db, app):
    if not db.get_contact_list():
        app.contact.create(ContactData(firstname="some contact"))
    return db.get_contact_list()


@given("a random contact from the list", target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)
    time.sleep(1)


@then('the new contact list is equal to the old contact list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=ContactData.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactData.id_or_max)


@when("I modify the contact from the list")
def modify_contact(app, random_contact, new_contact):
    app.contact.modify_contact_by_id(random_contact.id, new_contact)


@then("the new contact list is equal to the old contact list with the modified contact")
def verify_contact_modified(db, non_empty_contact_list, new_contact, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contact.id = random_contact.id
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactData.id_or_max) == sorted(app.group.get_group_list(), key=ContactData.id_or_max)
