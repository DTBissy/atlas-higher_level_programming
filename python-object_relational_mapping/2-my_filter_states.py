#!/usr/bin/python3
""" Creates a function that coneects to SQL Server"""
import MySQLdb
import sys


def print_user_state():
    """Imports database"""

    """Connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd="Gearsevenbb", db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\'{}' ORDER BY id;".format(sys.argv[4]))

    """THe data to be printed"""
    row = cur.fetchall()
    for row in row:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    print_user_state()
