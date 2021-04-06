import flask
from flask_login import LoginManager, login_required, login_user
from flask_login import logout_user
from forms import LoginForm
import click

from database import User, db

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'o4t4bnoto4yb9y6843q4b4n387q'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
@login_required
def index():
    return 'Hello'

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        user = User.select().where(User.email == form.email.data).get()

        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        # if not is_safe_url(next):
        #     return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for('index'))

@app.cli.command('create-database')
def create_database():
    db.create_tables([User])

@app.cli.command('create-user')
@click.argument('name')
@click.argument('email')
def create_user(name, email):
    User.create(name=name, email=email, password='123')
