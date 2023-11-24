#!/usr/bin/python3
"""Lists all states from hbtn_0e_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()

    mt = sys.argv[4]
    cursor.execute("""SELECT cities.name FROM cities
                   INNER JOIN states ON states.id=cities.state_id
                   WHERE states.name=%s""", (sys.argv[4],))
    records = cursor.fetchall()
    temp = list(row[0] for row in records)
    print(*temp, sep=", ")
    cursor.close()
    db.close()
