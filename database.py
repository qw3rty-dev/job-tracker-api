import sqlite3

def get_connection():
    conn= sqlite3.connect("jobs.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   create table if not exists jobs(
                   id integer primary key autoincrement,
                   title text,
                   company text,
                   location text,
                   link text unique,
                   applied integer default 0
                   )
                   """)
    conn.commit()
    conn.close()
    
