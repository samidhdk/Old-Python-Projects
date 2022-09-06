from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="template")
app.secret_key = "flasktest"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///santiagoramos.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.permanent_session_lifetime = timedelta(days=1000)
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), unique=True, nullable=False)
    tickets_collection = []

    def __init__(self, name):
        self.name = name


class Ticket():
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino



@app.route("/", methods=["POST", "GET"])
def home():

    if request.method == "POST":
        if "user" in session:
            origen = request.form["origen"]
            destino = request.form["destino"]
            ticket = Ticket(origen, destino)

            user = session["user"]
            find_user = Users.query.filter_by(name=user).first()

            find_user.tickets_collection.append(ticket)

            return redirect(url_for("apuntes"))
        else:
            return redirect(url_for("login"))

    return render_template("index.html")








@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        find_user = Users.query.filter_by(name=user).first()
        if not find_user:
            usr = Users(user)
            db.session.add(usr)
            db.session.commit()
        else:
            return redirect(url_for("home"))
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>Welcome {user} </h1>"
    else:
        return redirect(url_for("login"))


@app.route("/view")
def apuntes():
    if "user" in session:
        user = session["user"]
        find_user = Users.query.filter_by(name=user).first()
        return render_template("Inventario.html", values=find_user.tickets_collection)
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

