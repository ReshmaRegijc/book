from flask_login.utils import login_required
from book import app
from book import db
from book.models import Book, User
from book.forms import *
from flask import render_template, redirect,url_for, request, flash, abort
import os



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add', methods=['GET','POST'])
@login_required
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        author = form.author.data
        price = form.price.data

        new_book = Book(name,author,price)

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('list'))
    
    return render_template('add.html',form=form)

@app.route('/delete', methods=['GET','POST'])
@login_required
def delete():

    form = DeleteForm()

    if form.validate_on_submit():
        id = form.id.data

        buy_book = Book.query.get(id)

        db.session.delete(buy_book)
        db.session.commit()

        return redirect(url_for('list'))

    return render_template('delete.html',form=form)


@app.route('/list')
def list():
    books = Book.query.all()
    return render_template('list.html',books=books)






if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0", port = port)