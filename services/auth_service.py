import sqlite3
import bcrypt 

DB_NAME = "pony_archive.db"

def register_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    password_hash = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:
        cursor.execute(
            """
            INSERT INTO users(username, password_hash)
            VALUES (?, ?)
            """,
            (username, password_hash.decode())
        )

        conn.commit()

        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close() 
def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT password_hash
        FROM users
        WHERE username = ?
        """,
        (username,)
    )
    result = cursor.fetchone()
    conn.close()

    if result is None:
        return False
    stored_hash = result[0]

    return bcrypt.checkpw(
        password.encode(),
        stored_hash.encode()
    )