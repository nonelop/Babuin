import sqlite3
import time
import os

path = os.path.join(os.path.dirname(__file__), "database.db")

def new_profile(name: str, username: str | None):

    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO profiles (name, username, reg_time) VALUES (?, ?, ?)", (name, username, int(time.time())))
        connection.commit()
        profile_id = cursor.lastrowid
        return ("SUCCESSFUL", profile_id)

    except sqlite3.IntegrityError:
        return ("CONFLICT", None)

    finally:
        connection.close()

def get_profile(target: int | str):

    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    if type(target) is int:
        cursor.execute("SELECT * FROM profiles WHERE id = ?", (target,))
        
    elif type(target) is str:
        cursor.execute("SELECT * FROM profiles WHERE username = ?", (target,))

    profile = cursor.fetchone()

    if profile:
        return ("SUCCESSFUL", profile)
    else:
        return ("NOT_FOUND", None)