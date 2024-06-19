#!/usr/bin/python3
""" Creates a function that coneects to SQL Server"""
import MySQLdb
import sys

def print_state_n():
    """Imports database"""

    """Connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")

    """THe data to be printed"""
    row = cur.fetchall()
    for row in row:
        if str(row[1]).startswith("N"):
            print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    print_state_n()