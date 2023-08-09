import json
import os.path
import random
from fixture.application import Application
from fixture.db import DbFixture
from model.group import Group
from model.contactData import ContactData
import time


class AddressBook:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target["web"]
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])
        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
        db_config = self.target["db"]
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                                   password=db_config['password'])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    # groups
    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    # contacts
    def new_contact(self, firstname, lastname):
        return ContactData(firstname=firstname, lastname=lastname)

    def get_contact_list(self):
        time.sleep(1)
        return self.dbfixture.get_contact_list()

    def create_contact(self, contact):
        self.fixture.contact.create(contact)

    def random_contact(self, list):
        return random.choice(list)

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def create_contact_data(self, firstname, lastname):
        return ContactData(firstname=firstname, lastname=lastname)

    def modify_contact(self, contact, new_contact):
        new_contact.id = contact.id
        self.fixture.contact.modify_contact_by_id(contact.id, new_contact)

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=ContactData.id_or_max) == sorted(list2, key=ContactData.id_or_max)
