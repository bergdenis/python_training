from model.contactData import ContactData
import random
import string


constant = [
    ContactData(firstname="firstname1", lastname="lastname1", address="address1", email="email1", email2="email2",
                email3="email3", home_number="home_number1", mobile_number="mobile_number1", work_number="work_number1",
                secondary_number="secondary_number1"),
    ContactData(firstname="firstname2", lastname="lastname2", address="address2", email="email4", email2="email5",
                email3="email6", home_number="home_number2", mobile_number="mobile_number2", work_number="work_number2",
                secondary_number="secondary_number2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxlen):
    symbols = string.digits + "()-" + " "
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
