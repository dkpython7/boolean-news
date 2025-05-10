import sqlite3

# Connect to (or create) the feedback database
conn = sqlite3.connect('feedback.db')
cursor = conn.cursor()

# Create the feedback table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        predicted_label TEXT NOT NULL,
        actual_label TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Feedback database and table created successfully!")
