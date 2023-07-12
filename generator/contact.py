from model.contactData import ContactData
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
