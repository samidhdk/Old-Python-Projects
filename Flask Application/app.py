from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import timedelta

app = Flask(__name__, template_folder="template")
app.app_context().push()
app.secret_key = "flasktest"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///santiagoramos.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.permanent_session_lifetime = timedelta(days=1000)
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), unique=True, nullable=False)
    tickets_collections = db.relationship('Ticket', backref='user', lazy=True)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, origen, destino):
        self.user_id = user_id
        self.origen = origen
        self.destino = destino

    def __str__(self):
        return f"Ticket {self.id}: Origen: {self.origen}, Destino: {self.destino}"


@app.route("/", methods=["POST", "GET"])  # COMPRAR
def home():
    if request.method == "POST":
        if "user" in session:
            origen = request.form["origen"]
            destino = request.form["destino"]

            if origen != "" and destino != "":

                user = session["user"]
                find_user = Users.query.filter_by(name=user).first()

                nuevo_ticket = Ticket(user_id=find_user.id, origen=origen, destino=destino)

                db.session.add(nuevo_ticket)
                db.session.commit()
                print(nuevo_ticket.id)
                return redirect(url_for("ver_tickets"))
            else:
                pass
        else:
            return redirect(url_for("login"))

    return render_template("index.html")


#@app.route("/view", methods=['GET'])
@app.route("/view")
def ver_tickets():
    if "user" in session:

        if request.method == "GET":

            user = session["user"]
            find_user = Users.query.filter_by(name=user).first()

            for item in find_user.tickets_collections:
                print(item)

            return render_template("Inventario.html", values=find_user.tickets_collections)
        else:
            return render_template("rain.html")
    else:
        return redirect(url_for("login"))

@app.route("/eliminar_ticket/<int:ticket_id>", methods=['POST'])
def eliminar_ticket(ticket_id):
    if "user" in session:
        user = session["user"]
        find_user = Users.query.filter_by(name=user).first()
        ticket = Ticket.query.get(ticket_id)

        if ticket:
            if ticket.user_id is find_user.id:
                db.session.delete(ticket)
                db.session.commit()
    return redirect(url_for('ver_tickets'))

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


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
