#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
where name matches the argument, safe from MySQL injections.

Usage:
    ./script.py <mysql username> <mysql password> <database name> <state name searched>

Connects to localhost on port 3306.
Results sorted in ascending order by states.id.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # Requête SQL avec paramètre (sécurisée contre injection)
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Affichage des résultats
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
