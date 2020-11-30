import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learntest.settings')

import django
django.setup()


import random
from userslist.models import User
from faker import Faker

fake = Faker()

def populate(n=5):
    for entry in range(n):
        name = fake.name().split()
        fake_fname = name[0]
        fake_lname = name[1]
        fake_email = fake.email()

        use = User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_email)[0]

if __name__ == '__main__':
    populate(10)
