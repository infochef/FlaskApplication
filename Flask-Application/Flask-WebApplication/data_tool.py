import os
from flask import Flask, render_template, url_for, redirect, session
from forms import Addform, DelForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################
# SQL DATABASE AND MODELS
############################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()

db = SQLAlchemy(app)
Migrate(app, db)


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name,id):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Puppy name {self.name} is having id {self.id}"

db.create_all()


############################################
# VIEWS WITH FORMS
############################################

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_puppy():
    form = Addform()

    if form.validate_on_submit():
        name = form.name.data
        session['name'] = form.name.data

        # Add new Puppy to database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('thank_you'))

    return render_template('add.html', form=form)

@app.route('/thanks', methods=['GET', 'POST'])
def thank_you():
    return render_template('thankyou.html')

@app.route('/list')
def list_pup():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    print(puppies)
    return render_template('veiw.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
