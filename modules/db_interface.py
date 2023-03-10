import sqlite3
from flask_bcrypt import check_password_hash

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

def verify_user(username: str, password: str) -> bool:
    """Check if a user exists in the database"""

    if username == "" or password == "":
        return False

    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT username, password FROM users WHERE username=?', (username,))

    result = cur.fetchone()
    
    # If we find a user
    if result:
        pw_hash = result[1]
        if check_password_hash(pw_hash, password):
            return True

    # We did not find a user
    return False

def user_exists(username: str) -> bool:
    """ Check if a user exists in the database """
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT username FROM users WHERE username=?', (username,))

    result = cur.fetchone()

    # If we find the username
    if result:
        return True

    # We did not find the username
    return False
