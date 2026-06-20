import sqlite3


def create_database():

    conn = sqlite3.connect("pony_archive.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS figures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        owner_id INTEGER NOT NULL,

        name TEXT NOT NULL,
        character TEXT NOT NULL,

        series_name TEXT,

        figure_type TEXT NOT NULL,

        rarity TEXT,

        price REAL,

        purchase_date TEXT,

        condition TEXT,

        has_box INTEGER DEFAULT 0,

        image_path TEXT,

        notes TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(owner_id)
        REFERENCES users(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        action TEXT NOT NULL,

        description TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(user_id)
        REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

    print("БД создана")


if __name__ == "__main__":
    create_database()