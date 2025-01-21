# Modello Er
### Modello er
::: mermaid
erDiagram

    clienti ||--o{ ordini : effettua
    prodotti ||--o{ prodotti-ordini :contiene
    ordini ||--o{ prodotti-ordini : presente
    clienti ||--o{ recensioni: scrive
    prodotti ||--o{ recensioni: riceve

    prodotti {
        string nome
        string descrizione
        int prezzo
        string categoria
    }

    clienti {
        string nome
        string cognome
        string e-mail
        string indirizzo
    }

    ordini {
        datetime data_ordine
        datetime data_consegna
        string stato    
    }

    recensioni {
        int punteggio
        datetime data
        string commento
    }

    prodotti-ordini{
    }
    
:::

### Modello logico
::: mermaid
erDiagram

    clienti ||--o{ ordini : effettua
    prodotti ||--o{ prodotti-ordini :contiene
    ordini ||--o{ prodotti-ordini : presente
    clienti ||--o{ recensioni: scrive
    prodotti ||--o{ recensioni: riceve

    prodotti {
        int product_id PK
        string nome
        string descrizione
        int prezzo
        string categoria
    }

    clienti {
        int client_id PK
        string nome
        string cognome
        string e-mail
        string indirizzo
    }

    ordini {
        int order_id PK
        datetime data_ordine
        datetime data_consegna
        string stato    
    }

    recensioni {
        int review_id PK
        int punteggio
        datetime data
        string commento
    }

    prodotti-ordini{
        int id_prodotto PK,FK
        int id_ordine PK,FK
    }
    
:::

# Normalizzazione

- **PRODOTTI**: ProductID `PK`, nome, descrizione, prezzo, categoria
- **ORDINI**: OrderID `PK`, dataorigine, dataconsegna, stato
- **RECENSIONI**: ReviewID `PK`, punteggio, datarecensione, commento
- **CLIENTI**: ClientId `PK`, nome, cognome, email, indirizzo
- **PRODOTTI-ORDINI**: OrderID `FK` ProductID `FK`, `PK(OrderID, ProductID)`


# Database
```sql
CREATE DATABASE negozio;

CREATE TABLE clienti (
    ClientID int PRIMARY KEY,
    Nome varchar(255),
    Cognome varchar(255),
    Email varchar(255),
    Indirizzo varchar(255)
);

CREATE TABLE ordini (
    OrderID int PRIMARY KEY,
    DataOrigine date,
    DataConsegna date,
    Stato varchar(255),
);

CREATE TABLE prodotti (
    ProductID int PRIMARY KEY,
    Nome varchar(255),
    Descrizione varchar(255),
    Prezzo int,
    Categoria varchar(255),
);

CREATE TABLE recensioni (
    ReviewID int PRIMARY KEY,
    Punteggio int,
    DataRecensione date,
    Commento varchar(255)
);

CREATE TABLE Prodotti_Ordini (
    ProductID int,
    OrderID int,
    PRIMARY KEY (ProductID, OrderID),
    FOREIGN KEY (ProductID) REFERENCES Prodotti(ProductID),
    FOREIGN KEY (OrderID) REFERENCES Ordini(OrderID)
);
```
