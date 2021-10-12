from flask import Flask, render_template, request
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class User(db.Model):
    email = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


db.create_all()

archie = User(email="archie.andrews@email.com", password="football4life")
veronica = User(email="veronica.lodge@email.com", password="fashiondiva")

db.session.add(archie)
db.session.add(veronica)

try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
finally:
    db.session.close()

user = User.query.get("veronica.lodge@email.com")
db.session.delete(user)

try:
    db.session.commit()
except Exception as e:
    db.session.rollback()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # for u_email, u_password in users.items():
        #     if u_email == form.email.data and u_password == form.password.data:
        #         return render_template("login.html", message = "Successfully Logged In", form = form)
        return render_template("login.html", message ="Incorrect Email or Password", form = form)

    elif form.errors:
        print(form.errors.items())

    return render_template("login.html", form = form)


if __name__ == "__main__":
    app.run()
