CREATE DATABASE veille_ia_medecine;
USE veille_ia_medecine;

CREATE TABLE informations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(255) NOT NULL,
    description TEXT,
    url VARCHAR(255),
    date_publication DATE
);
