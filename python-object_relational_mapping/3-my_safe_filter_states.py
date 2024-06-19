#!/usr/bin/python3
""" Creates a function that coneects to SQL Server"""
import MySQLdb
import sys


def print_user_state():
    """Imports database"""

    """Connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    state_name = sys.argv[4].replace("'", "\\'")
    query = f"SELECT * FROM states WHERE name LIKE '{state_name}'\
                 ORDER BY id;"
    cur.execute(query)

    """THe data to be printed"""
    row = cur.fetchall()
    for row in row:
        if str(row[1]).
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    print_user_state()
