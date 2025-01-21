### Esercizio

Considera il seguente modello logico di un database che non rispetta la Prima Forma Normale (1NF), la Seconda Forma Normale (2NF) e la Terza Forma Normale (3NF):

#### Tabelle

- **STUDENT**: id `PK`, name, addresses, courses, advisor_id, advisor_name, advisor_office
- **COURSE**: id `PK`, name, student_ids

### Compito

1. Normalizza il modello logico del database per rispettare la Prima Forma Normale (1NF).
2. Porta il modello logico del database alla Seconda Forma Normale (2NF).
3. Porta il modello logico del database alla Terza Forma Normale (3NF).

### 1NF
- **STUDENT**: id `PK`, name, advisor_id, advisor_name, advisor_office
- **COURSE**: id `PK`, name

- **ADDRESS**: student_id `FK` STUDENT.id, address, `PK(student_id, address)`
- **STUDENT_COURSE**: student_id `FK`, course_id `FK`, `PK(student_id, course_id)`

### 2NF

- **STUDENT**: id `PK`, name, advisor_id, advisor_name, advisor_office
- **COURSE**: id `PK`, name
    
- **ADDRESS**: student_id `FK` STUDENT.id, address, `PK(student_id, address)`
- **STUDENT_COURSE**: student_id `FK`, course_id `FK`, `PK(student_id, course_id)`

### 3NF

- **STUDENT**: id `PK`, name, advisor_id `FK`
- **COURSE**: id `PK`, name

- **ADDRESS**: student_id `FK` STUDENT.id, address, `PK(student_id, address)`
- **STUDENT_COURSE**: student_id `FK`, course_id `FK`, `PK(student_id, course_id)`
- **ADVISOR**: id `PK`, name, office
