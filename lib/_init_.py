import sqlite3

CONN = sqlite3.connect('music_database.db')
CURSOR = CONN.cursor()