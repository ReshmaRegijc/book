from book.models import Book, User
from book import db
from werkzeug.security import generate_password_hash
#put in function

def test_Book():
    newbook = Book('Flask','ABC',500)

    db.session.add(newbook)
    db.session.commit()


    db.session.delete(newbook)
    db.session.commit()
    


    assert (1==1)

def test_User():


    pass_hash = generate_password_hash('password')

    new_user = User('reshma123@gmail.com','reshma123',pass_hash)

    db.session.add(new_user)
    db.session.commit()


    db.session.delete(new_user)
    db.session.commit()

    assert (1==1)
