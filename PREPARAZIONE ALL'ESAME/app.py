import sqlite3
import os
from datetime import datetime, time

# Percorso del database
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scuola.db')

def create_tables():
    """Crea le tabelle nel database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Tabella Tipologia Classe (liceo, tecnico, professionale)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tipologia_classe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    ''')
    
    # Tabella Indirizzo
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS indirizzo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipologia_id INTEGER NOT NULL,
        FOREIGN KEY (tipologia_id) REFERENCES tipologia_classe (id)
    )
    ''')
    
    # Tabella Articolazione
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS articolazione (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        indirizzo_id INTEGER NOT NULL,
        FOREIGN KEY (indirizzo_id) REFERENCES indirizzo (id)
    )
    ''')
    
    # Tabella Opzione
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS opzione (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        articolazione_id INTEGER,
        FOREIGN KEY (articolazione_id) REFERENCES articolazione (id)
    )
    ''')
    
    # Tabella Classe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS classe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        anno INTEGER NOT NULL,
        sezione TEXT NOT NULL,
        anno_scolastico TEXT NOT NULL,
        indirizzo_id INTEGER NOT NULL,
        articolazione_id INTEGER,
        opzione_id INTEGER,
        FOREIGN KEY (indirizzo_id) REFERENCES indirizzo (id),
        FOREIGN KEY (articolazione_id) REFERENCES articolazione (id),
        FOREIGN KEY (opzione_id) REFERENCES opzione (id)
    )
    ''')
    
    # Tabella Docente
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS docente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    
    # Tabella Studente
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS studente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL,
        data_nascita DATE NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        classe_id INTEGER NOT NULL,
        FOREIGN KEY (classe_id) REFERENCES classe (id)
    )
    ''')
    
    # Tabella Materia
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS materia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    ''')
    
    # Tabella Tipo Assenza
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tipo_assenza (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL
    )
    ''')
    
    # Tabella Assenza
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS assenza (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE NOT NULL,
        orario TIME,
        tipo_id INTEGER NOT NULL,
        studente_id INTEGER NOT NULL,
        docente_id INTEGER NOT NULL,
        FOREIGN KEY (tipo_id) REFERENCES tipo_assenza (id),
        FOREIGN KEY (studente_id) REFERENCES studente (id),
        FOREIGN KEY (docente_id) REFERENCES docente (id)
    )
    ''')
    
    # Tabella Ora Lezione
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ora_lezione (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE NOT NULL,
        ora_inizio TIME NOT NULL,
        ora_fine TIME NOT NULL,
        materia_id INTEGER NOT NULL,
        classe_id INTEGER NOT NULL,
        docente_id INTEGER NOT NULL,
        argomento TEXT,
        FOREIGN KEY (materia_id) REFERENCES materia (id),
        FOREIGN KEY (classe_id) REFERENCES classe (id),
        FOREIGN KEY (docente_id) REFERENCES docente (id)
    )
    ''')
    
    # Tabella Docenti Compresenti (relazione many-to-many)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS docente_compresente (
        ora_lezione_id INTEGER,
        docente_id INTEGER,
        PRIMARY KEY (ora_lezione_id, docente_id),
        FOREIGN KEY (ora_lezione_id) REFERENCES ora_lezione (id),
        FOREIGN KEY (docente_id) REFERENCES docente (id)
    )
    ''')
    
    conn.commit()
    conn.close()

def insert_sample_data():
    """Inserisce dati di esempio nel database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Inserimento tipologie di classe
    tipologie = [
        ('Liceo',),
        ('Tecnico',),
        ('Professionale',)
    ]
    cursor.executemany("INSERT INTO tipologia_classe (nome) VALUES (?)", tipologie)
    
    # Inserimento indirizzi
    indirizzi = [
        ('Classico', 1),  # Liceo Classico
        ('Scientifico', 1),  # Liceo Scientifico
        ('Informatica e Telecomunicazioni', 2),  # Tecnico Informatica
        ("Servizi per l'enogastronomia e l'ospitalità alberghiera", 3)  # Professionale Enogastronomia
    ]
    cursor.executemany("INSERT INTO indirizzo (nome, tipologia_id) VALUES (?, ?)", indirizzi)
    
    # Inserimento articolazioni
    articolazioni = [
        ('Informatica', 3),  # Articolazione Informatica per indirizzo Informatica e Telecomunicazioni
        ('Telecomunicazioni', 3),  # Articolazione Telecomunicazioni per indirizzo Informatica e Telecomunicazioni
        ('Enogastronomia', 4)  # Articolazione Enogastronomia per indirizzo Servizi per l'enogastronomia...
    ]
    cursor.executemany("INSERT INTO articolazione (nome, indirizzo_id) VALUES (?, ?)", articolazioni)
    
    # Inserimento opzioni
    opzioni = [
        ('Prodotti dolciari artigianali e industriali', 3)  # Opzione per Articolazione Enogastronomia
    ]
    cursor.executemany("INSERT INTO opzione (nome, articolazione_id) VALUES (?, ?)", opzioni)
    
    # Inserimento classi
    classi = [
        (5, 'A', '2023/2024', 3, 1, None),  # 5A Informatica
        (3, 'B', '2023/2024', 4, 3, 1),     # 3B Enogastronomia opzione Prodotti dolciari
        (1, 'C', '2023/2024', 1, None, None)  # 1C Classico
    ]
    cursor.executemany("INSERT INTO classe (anno, sezione, anno_scolastico, indirizzo_id, articolazione_id, opzione_id) VALUES (?, ?, ?, ?, ?, ?)", classi)
    
    # Inserimento docenti
    # Nota: in un'applicazione reale, le password dovrebbero essere criptate
    docenti = [
        ('Mario', 'Rossi', 'prof.rossi', 'password123', 'mario.rossi@scuola.it'),
        ('Anna', 'Bianchi', 'prof.bianchi', 'password456', 'anna.bianchi@scuola.it'),
        ('Giuseppe', 'Verdi', 'prof.verdi', 'password789', 'giuseppe.verdi@scuola.it')
    ]
    cursor.executemany("INSERT INTO docente (nome, cognome, username, password_hash, email) VALUES (?, ?, ?, ?, ?)", docenti)
    
    # Inserimento studenti
    studenti = [
        ('Luca', 'Ferrari', '2005-05-15', 'luca.ferrari', 'password123', 1),  # Luca Ferrari, 5A Informatica
        ('Giulia', 'Esposito', '2006-10-20', 'giulia.esposito', 'password456', 2),  # Giulia Esposito, 3B Enogastronomia
        ('Marco', 'Romano', '2007-03-08', 'marco.romano', 'password789', 3),  # Marco Romano, 1C Classico
        ('Elena', 'Conti', '2005-07-22', 'elena.conti', 'password321', 4),  # Elena Conti, 5A Informatica
    ]
    cursor.executemany("INSERT INTO studente (nome, cognome, data_nascita, username, password_hash, classe_id) VALUES (?, ?, ?, ?, ?, ?)", studenti)
    
    # Inserimento materie
    materie = [
        ('Informatica',),
        ('Italiano',),
        ('Matematica',),
        ('Inglese',),
        ('Sistemi e Reti',),
        ('Laboratorio di Pasticceria',)
    ]
    cursor.executemany("INSERT INTO materia (nome) VALUES (?)", materie)
    
    # Inserimento tipi di assenza
    tipi_assenza = [
        ('Giorno intero',),
        ('Ritardo',),
        ('Uscita anticipata',)
    ]
    cursor.executemany("INSERT INTO tipo_assenza (tipo) VALUES (?)", tipi_assenza)
    
    # Inserimento assenze
    assenze = [
        ('2023-11-15', None, 1, 1, 1),  # Luca Ferrari, assenza giorno intero, registrata da prof. Rossi
        ('2023-11-20', '08:30', 2, 2, 2),  # Giulia Esposito, ritardo alle 8:30, registrata da prof. Bianchi
        ('2023-11-22', '12:15', 3, 3, 3),  # Marco Romano, uscita anticipata alle 12:15, registrata da prof. Verdi
        # Aggiungiamo altre 20 assenze casuali
        ('2023-10-05', None, 1, 1, 2),  # Luca Ferrari, assenza giorno intero
        ('2023-10-12', None, 1, 2, 1),  # Giulia Esposito, assenza giorno intero
        ('2023-10-20', None, 1, 3, 3),  # Marco Romano, assenza giorno intero
        ('2023-10-25', '08:45', 2, 1, 3),  # Luca Ferrari, ritardo
        ('2023-11-02', '08:20', 2, 2, 2),  # Giulia Esposito, ritardo
        ('2023-11-05', '08:35', 2, 3, 1),  # Marco Romano, ritardo
        ('2023-11-08', '12:30', 3, 1, 2),  # Luca Ferrari, uscita anticipata
        ('2023-11-10', '12:45', 3, 2, 3),  # Giulia Esposito, uscita anticipata
        ('2023-11-13', '11:30', 3, 3, 1),  # Marco Romano, uscita anticipata
        ('2023-12-01', None, 1, 1, 3),  # Luca Ferrari, assenza giorno intero
        ('2023-12-05', None, 1, 2, 2),  # Giulia Esposito, assenza giorno intero
        ('2023-12-08', None, 1, 3, 1),  # Marco Romano, assenza giorno intero
        ('2023-12-12', '08:15', 2, 1, 1),  # Luca Ferrari, ritardo
        ('2023-12-15', '08:40', 2, 2, 3),  # Giulia Esposito, ritardo
        ('2024-01-10', '08:25', 2, 3, 2),  # Marco Romano, ritardo
        ('2024-01-15', '11:50', 3, 1, 3),  # Luca Ferrari, uscita anticipata
        ('2024-01-20', '12:20', 3, 2, 1),  # Giulia Esposito, uscita anticipata
        ('2024-01-25', '12:35', 3, 3, 2),  # Marco Romano, uscita anticipata
        ('2024-02-05', None, 1, 1, 1),  # Luca Ferrari, assenza giorno intero
        ('2024-02-12', '08:10', 2, 2, 2)   # Giulia Esposito, ritardo
    ]
    cursor.executemany("INSERT INTO assenza (data, orario, tipo_id, studente_id, docente_id) VALUES (?, ?, ?, ?, ?)", assenze)
    
    # Inserimento ore di lezione
    ore_lezione = [
        ('2023-11-15', '08:00', '09:00', 1, 1, 1, 'Programmazione orientata agli oggetti'),  # Informatica in 5A
        ('2023-11-15', '09:00', '10:00', 2, 1, 2, 'Analisi del testo'),  # Italiano in 5A
        ('2023-11-16', '10:00', '11:00', 6, 2, 3, 'Preparazione dolci da forno')  # Laboratorio Pasticceria in 3B
    ]
    cursor.executemany("INSERT INTO ora_lezione (data, ora_inizio, ora_fine, materia_id, classe_id, docente_id, argomento) VALUES (?, ?, ?, ?, ?, ?, ?)", ore_lezione)
    
    # Inserimento docenti compresenti
    docenti_compresenti = [
        (3, 2)  # Prof. Bianchi come docente compresente nella lezione di Laboratorio di Pasticceria
    ]
    cursor.executemany("INSERT INTO docente_compresente (ora_lezione_id, docente_id) VALUES (?, ?)", docenti_compresenti)
    
    conn.commit()
    conn.close()

def main():
    """Funzione principale"""
    # Controlla se il database esiste già
    db_exists = os.path.exists(DB_PATH)
    
    # Crea le tabelle
    create_tables()
    
    # Se il database è stato appena creato, inserisci i dati di esempio
    if not db_exists:
        insert_sample_data()
        print(f"Database creato con successo in: {DB_PATH}")
        print("Dati di esempio inseriti.")
    else:
        print(f"Database esistente aggiornato in: {DB_PATH}")

if __name__ == "__main__":
    main()
