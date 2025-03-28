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


@app.teardown_appcontext
def close_db(error):
    """Chiude la connessione al database"""
    if hasattr(g, "db"):
        g.db.close()

@app.route("/raw_giocatori")
def raw_giocatori():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM GIOCATORE")
    entries = cursor.fetchall()
    cursor.close()
    return jsonify([dict(row) for row in entries])

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/giocatori")
def giocatori():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT g.*, a.nome as allenatore_nome, a.cognome as allenatore_cognome 
        FROM GIOCATORE g 
        LEFT JOIN ALLENATORE a ON g.allenatore_id = a.id
    """)
    entries = cursor.fetchall()
    # Fetch allenatore data for additional context if needed
    cursor.execute("SELECT id, nome, cognome FROM ALLENATORE")
    entrieses = cursor.fetchall()
    cursor.close()
    return render_template("giocatori.html", entries=entries, entrieses=entrieses)

@app.route("/allenatore")
def allenatore():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, cognome FROM ALLENATORE")
    entrieses = cursor.fetchall()
    cursor.close()
    return render_template("allenatore.html", entrieses=entrieses)

@app.route("/squadre")
def squadre():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, data FROM ")
    entries = cursor.fetchall()
    cursor.close()
    return render_template("squadre.html", entries=entries)

if __name__ == "__main__":
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True, port=50849)