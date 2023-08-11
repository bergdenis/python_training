from model.contactData import ContactData
import random
import allure


def test_modify_contact_lastname(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(ContactData(lastname="Test"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    modified_contact = ContactData(lastname="new last name", id=str(contact.id))
    with allure.step('When I modify a contact %s from the list' % contact):
        app.contact.modify_contact_by_id(contact.id, modified_contact)
    with allure.step('Then the new contact list is equal to the old contact list with the modified contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        for i, c in enumerate(old_contacts):
            if c.id == contact.id:
                old_contacts[i] = modified_contact
                break
        assert sorted(old_contacts, key=ContactData.id_or_max) == sorted(new_contacts, key=ContactData.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=ContactData.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactData.id_or_max)
