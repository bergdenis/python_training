# -*- coding: utf-8 -*-
import pytest
from model.contactData import ContactData
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(ContactData(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="ttl", company="cmp", address="adr1", home_number="111111", mobile_number="222222", work_number="333333", fax_number="444444",
                        email="mail@mail.com", email2="mail2@mail.com", email3="mail3@mail.com", homepage="www.hopg.com", bday="7", bmonth="July", byear="1977",
                        aday="10", amonth="October", ayear="2010", address2="adr2", phone2="555555", notes="test"))
    app.session.logout()
