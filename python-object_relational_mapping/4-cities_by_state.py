#!/usr/bin/python3
""" Lists all cities"""
import MySQLdb
import sys


def list_cities():
    """Works on database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id;"
    cur.execute(query)

    row = cur.fetchall()
    for row in row:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    list_cities()
    