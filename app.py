
from book import app
from book import db
from book.models import Book
from book.forms import *
from flask import render_template, redirect,url_for, request, flash
from flask_dance.contrib.google import make_google_blueprint, google
import os
from flask_login import logout_user

from book import blueprint


@app.route('/')
def index():
    books = Book.query.all()
    #,books=books
    return render_template('home.html',books=books)

@app.route('/welcome')
def welcome_user():
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]
    return render_template('home.html')


@app.route('/add', methods=['GET','POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        author = form.author.data
        price = form.price.data

        new_book = Book(name,author,price)

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('index'))
    
    return render_template('add.html',form=form)

@app.route('/delete', methods=['GET','POST'])
def delete():

    form = DeleteForm()

    if form.validate_on_submit():
        id = form.id.data

        buy_book = Book.query.get(id)

        db.session.delete(buy_book)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('delete.html',form=form)



@app.route("/login/google")
def login():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("home.html",email=email)

@app.route("/logout")
def logout():
    flash('You logged out!')
    token = blueprint.token["access_token"]
    resp = google.post(
        "https://accounts.google.com/o/oauth2/revoke",
        params={"token": token},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert resp.ok, resp.text
    logout_user()        # Delete Flask-Login's session cookie
    del blueprint.token  # Delete OAuth token from storage

    return redirect(url_for('index'))


if __name__=='__main__':
    #port = int(os.environ.get('PORT', 5000))
    #,host="0.0.0.0", port = port
    app.run(debug=True)


