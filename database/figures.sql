CREATE TABLE IF NOT EXISTS figures(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    name TEXT NOT NULL,

    type TEXT,

    series TEXT,

    rarity TEXT,

    purchase_date TEXT,

    price REAL,

    condition TEXT,

    quantity INTEGER,

    note TEXT,

    image_path TEXT,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

);