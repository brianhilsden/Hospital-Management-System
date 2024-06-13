import sqlite3

conn = sqlite3.connect('./lib/database/zawadihospital.db')
cursor = conn.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')
