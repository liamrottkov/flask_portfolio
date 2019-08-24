from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import ContactForm
from app.models import Contact


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')

@app.route('/about')
def about():

    return render_template('about.html', title='About')

@app.route('/projects')
def projects():
    products = [
        {
            'id': 1001,
            'title': 'Hangman',
            'desc': 'Hangman game created using Python 3.',
            'url': '../static/images/hangman.jpg',
            'source': 'https://github.com/liamrottkov/hangman/blob/master/hangman.ipynb'
        },
        {
            'id': 1002,
            'title': 'Blackjack',
            'desc': 'Blackjack game created using Python 3.',
            'url': '../static/images/blackjack.jpg',
            'source': 'https://github.com/liamrottkov/blackjack/blob/master/blackjack.ipynb'
        },
        {
            'id': 1003,
            'title': 'Twitter E-Commerce Website',
            'desc': 'Twitter-style social network and E-commerce website created using HTML 5, CSS 3, Boostrap 4, Flask, and Python 3',
            'url': '../static/images/twitter_commerce.jpg',
            'source': 'https://github.com/liamrottkov/twitter_commerce'

        },
        {
            'id': 1004,
            'title': 'Monster Dungeon Game',
            'desc': 'Monster dungeon game created using Python 3.',
            'url': '../static/images/monster_dungeon.jpg',
            'source': 'https://github.com/liamrottkov/monster_dungeon/blob/master/monster_dungeon.ipynb'
        },
        {
            'id': 1005,
            'title': 'Amazon Sign-In Page',
            'desc': 'Amazon Sign-In page replicated using HTML, CSS, and Bootstrap',
            'url': '../static/images/amazon.jpg',
            'source': 'https://github.com/liamrottkov/amazon_login'
        },
        {
            'id': 1006,
            'title': 'Weather Mobile App',
            'desc': 'Weather App created using React Native',
            'url': '../static/images/1.jpg',
            'source': 'https://github.com/liamrottkov/weather_mobile_app'
        },
    ]


    return render_template('projects.html', products=products, title='Projects')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():

        contact = Contact(
            name = form.name.data,
            email = form.email.data,
            message = form.message.data
        )

        db.session.add(contact)
        db.session.commit()

        flash("Thanks for contacting me, I will be in touch soon!")

        return redirect(url_for('contact'))


    return render_template('contact.html', form=form, title='Contact')
