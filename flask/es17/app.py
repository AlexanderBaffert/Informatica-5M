import json
import sqlite3
from flask import Flask, g, jsonify, render_template
import os


app = Flask(__name__)
app.secret_key = "your-secret-key-here"

# Build the path to config.json relative to this file
config_path = os.path.join(os.path.dirname(__file__), "config.json")
with open(config_path) as config_file:
    config = json.load(config_file)
    DATABASE = config["DATABASE"]
    INITIALIZATION = config["INITIALIZATION"]


def get_db():
    """Connessione al database"""
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


def init_db():
    """Inizializza il database"""
    with app.app_context():
        db = get_db()
        # Load schema from queries folder
        with app.open_resource(INITIALIZATION) as f:
            db.executescript(f.read().decode("utf8"))
        db.commit()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/telescopi")
def telescopi():
    db = get_db()
    cur = db.execute("SELECT id, nome, posizione, apertura, tipo FROM TELESCOPIO")
    telescopi = cur.fetchall()
    return render_template("telescopi.html", telescopi=telescopi)

@app.route("/corpi")
def corpi():
    db = get_db()
    cur = db.execute("SELECT id, nome, categoria, magnitudine, distanza_parsec FROM CORPO_CELESTE")
    corpi = cur.fetchall()
    return render_template("corpi.html", corpi=corpi)

@app.route("/ricercatore")
def ricercatori():
    db = get_db()
    cur = db.execute("SELECT id, nome, cognome, email, istituzione FROM RICERCATORE")
    ricercatori = cur.fetchall()
    return render_template("ricercatori.html", ricercatori=ricercatori)

if __name__ == "__main__":
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True, port=50849)