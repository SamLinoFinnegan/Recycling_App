import os
from hashlib import sha3_512
import csv



PATH_IMG = os.path.join(os.getcwd(), os.path.join(os.path.basename("static"), os.path.basename("images")))


def hash_password(password):
    return sha3_512(password.encode("utf-8")).hexdigest()

def populate_test_database():
    from models import User ,Product, products_db

    products_db.create_tables([Product, User])

    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            Product.create(name=row["name"], pack=row["pack"], trigger=row["trigger"], bin=row["bin"])
    

    hashed_password = hash_password("SamIsthebestBrotherEver")

    User.create(name="ana@anasemail.com", password=hashed_password)





if not os.path.isfile(os.path.join(os.getcwd(), os.path.basename("Products.db"))):
    populate_test_database()
