import sqlite3

def new_profile(name: str, username: str | None):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO profiles (name, username) VALUES (?, ?)", (name, username))

    connection.commit()

    connection.close()
    cursor.close()