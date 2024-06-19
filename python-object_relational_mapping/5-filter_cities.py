#!/usr/bin/python3
""" TAkes the name of a cuty in as a arg"""
import MySQLdb
import sys


def usr_city_search():
    """The city searcher"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    
    cur = db.cursor()
    # state_name = sys.argv[4].replace('"', "\\'")
    cur.execute(f"SELECT cities.name FROM cities JOIN states ON cities.state_id\
        = states.id WHERE states.name LIKE {sys.argv[4]} ORDER BY\
            cities.id;")
    
    print(", ".join(rows[0] for rows in cur.fetchall()))
  
    cur.close()
    db.close()


if __name__ == "__main__":
    usr_city_search()

    