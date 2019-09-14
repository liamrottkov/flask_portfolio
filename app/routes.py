from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import ContactForm
from app.models import Contact
from app.email import sendEmail


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
            'title': 'eCommerce Website',
            'desc': 'Created a full-stack eCommerce website that implements ReactJS frontend, Flask backend, SQL database, email support, Stripe payment API, and user authentication. Hosted on Heroku at https://ecommerce-website-frontend.herokuapp.com/ (link located on the NavBar above).',
            'url': '../static/images/ecommerce.jpg',
            'source': 'https://github.com/liamrottkov/ecommerce_website_frontend'
        },
        {
            'id': 1002,
            'title': 'Tic-Tac-Toe mobile',
            'desc': 'Tic-Tac-Toe mobile game created using React Native',
            'url': '../static/images/tictac.jpg',
            'source': 'https://github.com/liamrottkov/tic-tac-toe'
        },
        {
            'id': 1003,
            'title': 'Law Site Replica',
            'desc': 'Law site replica created using HTML, CSS, and Bootstrap',
            'url': '../static/images/lawsite.jpg',
            'source': 'https://github.com/liamrottkov/law_site_replica'

        },
        {
            'id': 1004,
            'title': 'Blackjack',
            'desc': 'Blackjack game created using Python 3.',
            'url': '../static/images/blackjack.jpg',
            'source': 'https://github.com/liamrottkov/blackjack/blob/master/blackjack.ipynb'
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
        {
            'id': 1007,
            'title': 'Hangman',
            'desc': 'Hangman game created using Python 3.',
            'url': '../static/images/hangman.jpg',
            'source': 'https://github.com/liamrottkov/hangman/blob/master/hangman.ipynb'
        },
        {
            'id': 1008,
            'title': 'Twitter-style social network',
            'desc': 'Twitter-style social network and eCommerce website created using HTML 5, CSS 3, Boostrap 4, Flask, and Python 3',
            'url': '../static/images/twitter_commerce.jpg',
            'source': 'https://github.com/liamrottkov/twitter_commerce'

        },
        {
            'id': 1009,
            'title': 'Monster Dungeon Game',
            'desc': 'Monster dungeon game created using Python 3.',
            'url': '../static/images/monster_dungeon.jpg',
            'source': 'https://github.com/liamrottkov/monster_dungeon/blob/master/monster_dungeon.ipynb'
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

        sendEmail(form.name.data, form.email.data, form.message.data)

        flash("Thanks for contacting me, I will be in touch soon!")

        return redirect(url_for('contact'))


    return render_template('contact.html', form=form, title='Contact')
