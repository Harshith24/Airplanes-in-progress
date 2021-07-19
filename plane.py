import sqlite3

def view():
    conn = sqlite3.connect("C:\\sqlite\\AprData")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Apr")
    rows = cur.fetchall()
    print(rows)

def insert():
    conn = sqlite3.connect("C:\\sqlite\\AprData")
    cur=conn.cursor()
    cur.execute("INSERT INTO Apr Values (400, 8000)")
    conn.commit()
    conn.close

def create():
    conn = sqlite3.connect("C:\\sqlite\\AprData")
    cur=conn.cursor()
    cur.execute("CREATE TABLE Apr (Type TEXT, Passengers INTEGER, Range INTEGER, Weight INTEGER, mpg INTEGER)")
    conn.commit()
    conn.close

def drop():
    conn = sqlite3.connect("C:\\sqlite\\AprData")
    cur=conn.cursor()
    cur.execute("DROP TABLE Apr")
    conn.commit()
    conn.close()

#insert()
#view()
#create()
#drop()