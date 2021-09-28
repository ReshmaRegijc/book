from book.models import Book
from book import db
#put in function

def test_Book():
    newbook = Book('Flask','ABC',500)

    db.session.add(newbook)
    x = db.session.commit()

    books = Book.query.all()
    for book in books:
        print(book)


    print(x)
    assert (1==1)
