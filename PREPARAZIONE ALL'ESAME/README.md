# Sistema di Gestione Assenze Scolastiche

Questa applicazione web consente la gestione delle assenze degli studenti di una scuola superiore, utilizzando Flask e SQLAlchemy.

## Funzionalità

- **Gestione degli utenti** (studenti e docenti)
- **Registrazione delle assenze** (giorno intero, ritardo, uscita anticipata)
- **Registrazione delle lezioni** con argomenti trattati
- **Gestione delle classi** con tipologie, indirizzi, articolazioni e opzioni
- **Gestione delle compresenze** per docenti di laboratorio e sostegno

## Struttura del Database

Il database è organizzato secondo le seguenti entità:

1. **Utenti**:
   - Studenti (con username/password per accesso)
   - Docenti

2. **Classi**:
   - Tipologia (liceo, tecnico, professionale)
   - Indirizzo
   - Articolazione (opzionale)
   - Opzione (opzionale)

3. **Assenze**:
   - Giorno intero
   - Ritardo (con orario)
   - Uscita anticipata (con orario)

4. **Lezioni**:
   - Ore di lezione svolte
   - Docenti principali e compresenti
   - Materie e argomenti trattati

## Requisiti

- Python 3.7+
- Flask
- Flask-SQLAlchemy
- Werkzeug

## Installazione

1. Clona il repository
2. Installa le dipendenze:
   ```
   pip install -r requirements.txt
   ```
3. Esegui l'applicazione:
   ```
   python app.py
   ```

## Utilizzo

- **Studenti**: possono visualizzare le proprie assenze
- **Docenti**: possono registrare assenze, lezioni e firmare compresenze

## Dati di accesso demo

- **Docente**:
  - Username: prof1
  - Password: password1

- **Studente**:
  - Username: stud1
  - Password: password3
