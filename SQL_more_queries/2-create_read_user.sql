-- Crée la base de données hbtn_0d_2 si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Crée l'utilisateur user_0d_2 si il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Donne uniquement le privilège SELECT sur la base hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Recharge les privilèges pour qu'ils soient pris en compte immédiatement
FLUSH PRIVILEGES;
