SELECT s.nome, s.cognome, a.data, a.orario
FROM studente s
JOIN assenza a ON s.id = a.id 
WHERE s.id  = 4  -- Sostituisci con l'ID dello studente specifico
-- oppure
-- WHERE s.nome = :nome AND s.cognome = :cognome
ORDER BY a.data ASC;

----- 2 

-- Elenco degli studenti che non hanno mai fatto assenze
SELECT s.id, s.nome, s.cognome, c.anno, c.sezione
FROM studente s
LEFT JOIN classe c ON s.classe_id = c.id
WHERE s.id NOT IN (
    SELECT DISTINCT studente_id
    FROM assenza
)
ORDER BY s.cognome, s.nome;

SELECT s.nome, s.cognome, c.nome_classe
FROM STUDENTE s
JOIN CLASSE c ON s.id_classe = c.id_classe
LEFT JOIN ASSENZA a ON s.id_studente = a.id_studente
WHERE a.id_assenza IS NULL
ORDER BY c.nome_classe, s.cognome, s.nome;