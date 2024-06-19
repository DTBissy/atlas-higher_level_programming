#!/usr/bin/python3
""" Lists all cities"""
import MySQLdb
import sys


def list_cities():
    """Works on database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    
    cur = db.cursor()
    query = "SELECT * FROM cities ORDER BY id ASC;"
    cur.execute(query)

    for row in row:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    list_cities()