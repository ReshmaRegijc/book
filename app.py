
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


"""@app.route('/logout')
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('index'))"""

"""@app.route('/login', methods= ['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully')

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('welcome_user')

            return redirect(next)

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for Registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)"""





if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    #,host="0.0.0.0", port = port
    app.run(debug=True,host="0.0.0.0", port = port)


