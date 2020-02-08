import sqlite3

def connect():
    conn=sqlite3.connect("tarns.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOOT EXISTS translated (word INTEGER, language INTEGER, t_word INTEGER )")
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("trans.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM transalted")
    row=cur.fetchall()
    conn.close()
    return row

def insert():
    conn=sqlite3.connect("trans.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO translated VALUES (NULL,?,?,?)",(word, language,t_word))
    conn.commit()
    conn.close()
    view()

connect()
