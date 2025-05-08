import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('register.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Create suggestion table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS suggestion (
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )
''')

# Commit and close connection
conn.commit()
conn.close()

print("Database and tables created successfully.")
