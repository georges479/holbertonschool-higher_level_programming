#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
where name matches the argument.

Usage:
    ./script.py <mysql username> <mysql password>
    <database name> <state name searched>

Connects to localhost on port 3306.
Uses string formatting to create the SQL query.
Results sorted by states.id in ascending order.
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

    # Construction de la requête SQL avec format()
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC").format(sys.argv[4])

    cursor.execute(query)

    # Affichage des résultats
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
