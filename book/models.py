from book import db

class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    author = db.Column(db.Text)
    price = db.Column(db.Integer)

    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price

    def __repr__(self):
        return (f"{self.id} Name:{self.name}; Author:{self.author}; Price:{self.price}")