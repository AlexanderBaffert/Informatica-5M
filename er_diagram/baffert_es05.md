### Versione 1
::: mermaid
erDiagram

    clienti ||--o{ ordini : effettua
    prodotti ||--o{ prodotti-ordini :contiene
    prodotti-ordini ||--o{ ordini: presente
    clienti ||--o{ recensioni: scrive

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

### Versione 2
::: mermaid
erDiagram

    clienti ||--o{ ordini : effettua
    prodotti ||--o{ prodotti-ordini :contiene
    prodotti-ordini ||--o{ ordini: presente
    clienti ||--o{ recensioni: scrive

    prodotti {
        int id PK
        string nome
        string descrizione
        int prezzo
        string categoria
        int id_prodotto FK
    }

    clienti {
        int id PK
        string nome
        string cognome
        string e-mail
        string indirizzo
    }

    ordini {
        int id PK
        datetime data_ordine
        datetime data_consegna
        string stato    
        int id_ordine FK
    }

    recensioni {
        int id PK
        int punteggio
        datetime data
        string commento
    }

    prodotti-ordini{
        int id_prodotto PK,FK
        int id_ordine PK,FK
    }
    
:::