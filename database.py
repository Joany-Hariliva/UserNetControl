import sqlite3

def create_connection():
    conn = sqlite3.connect('users.db')
    return conn

def create_table():
    conn = create_connection()
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        email TEXT NOT NULL,
                        role TEXT NOT NULL
                    );''')

def add_user(username, password, email, role):
    conn = create_connection()
    with conn:
        conn.execute('INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?);',
                     (username, password, email, role))

def delete_user(user_id):
    conn = create_connection()
    with conn:
        conn.execute('DELETE FROM users WHERE id=?;', (user_id,))

def update_user(user_id, username, password, email, role):
    conn = create_connection()
    with conn:
        conn.execute('''UPDATE users
                        SET username=?, password=?, email=?, role=?
                        WHERE id=?;''', (username, password, email, role, user_id))

def get_users():
    conn = create_connection()
    with conn:
        return conn.execute('SELECT * FROM users;').fetchall()
