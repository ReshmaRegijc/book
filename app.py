from flask_login.utils import login_required, login_user, logout_user
from book import app
from book import db
from book.models import Book, User
from book.forms import *
from flask import render_template, redirect,url_for, request, flash
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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))

@app.route('/login', methods= ['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully')

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('index')

            return redirect(next)

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET','POST'])
def register():

    form = RegistrationForm

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        user = User(email,username,password)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for Registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)







if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0", port = port)