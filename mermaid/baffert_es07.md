## Versione 1
::: mermaid
erDiagram
    Medico ||--o{ Specializzazione : ha
    Paziente ||--o{ Visita : prenota
    Medico ||--o{ Visita : effettua
    SalaVisita ||--o{ Visita : ospita
    Attrezzatura ||--o{ SalaVisita : contiene

    Medico {
        string nome
        string cognome
        string email
        string password
    }
    Paziente {
        string nome
        string cognome
        string email
        string password
    }
    Specializzazione {
        string nome
    }
    Visita {
        string descrizione
        int durata
        string preparazioni
        string data
    }
    SalaVisita {
        string nome
        string descrizione
    }
    Attrezzatura {
        string nome
        string descrizione
    }
:::

## Versione 2
::: mermaid
erDiagram
    Medico ||--o{ Specializzazione : ha
    Paziente ||--o{ Visita : prenota
    Medico ||--o{ Visita : effettua
    Paziente ||--o{ CartellaClinica : possiede
    CartellaClinica ||--o{ Visita : contiene
    SalaVisita ||--o{ Visita : ospita
    Attrezzatura ||--o{ SalaVisita : contiene

    Medico {
        int id PK
        string nome
        string cognome
        string email
        string password
    }
    Paziente {
        int id PK
        string nome
        string cognome
        string email
        string password
    }
    Specializzazione {
        int id PK
        string nome
    }
    Visita {
        int id PK
        int medico_id FK
        int paziente_id FK
        string descrizione
        int durata
        string preparazioni
        string data
    }
    CartellaClinica {
        int id PK
        int paziente_id FK
        string dettagli
    }
    SalaVisita {
        int id PK
        string nome
        string descrizione
    }
    Attrezzatura {
        int id PK
        string nome
        string descrizione
        int sala_id FK
    }
:::

