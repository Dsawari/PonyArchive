import sqlite3


DB = "pony_archive.db"



def add_figure(data):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute("""

    INSERT INTO figures(

        owner_id,

        name,

        character,

        series_name,

        figure_type,

        rarity,

        price,

        purchase_date,

        condition,

        image_path,

        notes

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?)

    """,

    (

        1,

        data["name"],

        data["name"],

        data["series"],

        data["type"],

        data["rarity"],

        data["price"],

        data["date"],

        data["condition"],

        data["image"],

        data["note"]

    ))


    conn.commit()

    conn.close()



def get_figures():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT * FROM figures
        """
    )


    figures = cursor.fetchall()


    conn.close()


    return figures