import sqlite3

def init_users_table() -> None:
    """Ensure the database and users table exists"""
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users(username TEXT NOT NULL, password TEXT NOT NULL);')
    con.commit()
    con.close()

def register_user_to_db(username: str, password: str) -> None:
    """Register a new user into the database"""
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(username, password) values(?, ?);', (username, password))
    con.commit()
    con.close()

def check_user(username: str, password: str) -> bool:
    """Check if a user exists in the database"""
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT username, password FROM users WHERE username=? and password=?', (username, password))

    result = cur.fetchone()
    
    if result:
        return True

    return False