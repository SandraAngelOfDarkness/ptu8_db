CREATE TABLE coder (
    id INTEGER PRIMARY KEY NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(200) UNIQUE,
    age INTEGER CHECK (age > 17 AND age < 75),
    experience INTEGER CHECK (experience < 40)
);

INSERT INTO coder (first_name, last_name, email, age, experience)
VALUES ("Kestutis", "Januskevicius", "kestas@midonov.fi", 39, 25);

INSERT INTO coder (first_name, last_name, email, age, experience)
VALUES ("Emilija", "Grybaite", "stas@midonov.fi", 19, 22);
SELECT * FROM coder;

-- jei reikia perkurti lentele
DROP TABLE coder;
ALTER TABLE coder ADD COLUMN project_id INTEGER;
ALTER TABLE coder ADD COLUMN teams_id INTEGER;
ALTER TABLE coder RENAME COLUMN teams_id to team_id;