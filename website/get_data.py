import sqlite3

def connect_db(db):
    try:
        my_db=sqlite3.connect(db)
    except Exception as e:
        print("Can't connect to db :" + str(e))
    return my_db

def close_connection(db):
    try:
        db.close()
    except Exception as e:
        print("Can't close db :" + str(e))

def select(db, table, attr='*'):
    query = "SELECT " + attr + " FROM " + table
    try:
        rows = db.execute(query)
    except Exception as e:
        print("Can't realise query :" + str(e))
    return rows

def select_where(db, table, atrr='*', condition):
    query = "SELECT " + attr + " FROM " + table + " WHERE " + condition
    try:
        rows = db.execute(query)
    except Exception as e:
        print("Can't realise query :" + str(e))
    return rows

def delete(db, table, condition):
    query = "DELETE FROM" + table + " WHERE " + condition
    try:
        db.execute(query)
    except Exception as e:
        print("Can't delete in db :" + str(e))