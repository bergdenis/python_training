from model.contactData import ContactData


def test_edit_first_contact(app):
    app.contact.edit_first_contact(ContactData(firstname="first name", middlename="middle name", lastname="last name", nickname="nick name", title="title", company="company", address="address", home_number="123456", mobile_number="234567", work_number="345678", fax_number="456789",
                                   email="mail@mail.cz", email2="mail2@mail.cz", email3="mail3@mail.cz", homepage="www.homepage.com", bday="8", bmonth="August", byear="1988",
                                   aday="11", amonth="November", ayear="2011", address2="address2", phone2="567890", notes="text text"))
