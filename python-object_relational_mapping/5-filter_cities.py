#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.

Usage:
    ./script.py <mysql username> <mysql password> <database name> <state name>

Connects to localhost on port 3306.
Results sorted by cities.id in ascending order.
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

    # Requête sécurisée avec jointure et paramètre
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (sys.argv[4],))

    # Récupération et affichage des villes
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    cursor.close()
    db.close()
