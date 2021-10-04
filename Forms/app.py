from flask import Flask, render_template, request
from forms import LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

users = {
    "archie.andrews@email.com": "football4life",
    "veronica.lodge@email.com": "fashiondiva"
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login.html", message = "Successfully Logged In", form = form)
        return render_template("login.html", message ="Incorrect Email or Password", form = form)

    elif form.errors:
        print(form.errors.items())

    return render_template("login.html", form = form)


if __name__ == "__main__":
    app.run()
