from model.contactData import ContactData


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactData(firstname="Test"))
    app.contact.delete_first_contact()
