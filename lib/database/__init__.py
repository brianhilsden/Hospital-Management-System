import sqlite3

# Connecting to the SQLite database file
conn = sqlite3.connect('./lib/database/zawadihospital.db')

# Creating a cursor object to interact with the database
cursor = conn.cursor()

# Enabling foreign key support
cursor.execute('PRAGMA foreign_keys = ON;')