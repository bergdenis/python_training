from model.contactData import ContactData


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(ContactData(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="ttl", company="cmp", address="address", home_number="111111", mobile_number="222222", work_number="333333", fax_number="444444",
                                   email="mail@mail.com", email2="mail2@mail.com", email3="mail3@mail.com", homepage="www.hopg.cz", bday="7", bmonth="July", byear="1977",
                                   aday="11", amonth="November", ayear="2011", address2="adr2", phone2="555555", notes="text text"))
    app.session.logout()
