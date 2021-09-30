from book.models import Book
from book import db
#put in function

def test_Book():
    newbook = Book('Flask','ABC',500)

    db.session.add(newbook)
    db.session.commit()


    db.session.delete(newbook)
    db.session.commit()
    


    assert (1==1)
