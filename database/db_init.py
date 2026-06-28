import sqlite3
import os
import sys

# Add parent directory to path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

def init_db():
    """Reads schema.sql and initializes the SQLite database."""
    print(f"Initializing database at: {Config.DATABASE_PATH}")
    
    # Ensure database directory exists
    os.makedirs(os.path.dirname(Config.DATABASE_PATH), exist_ok=True)
    
    conn = None
    try:
        # Connect to SQLite (creates the file if it doesn't exist)
        conn = sqlite3.connect(Config.DATABASE_PATH)
        
        # Enable foreign keys
        conn.execute("PRAGMA foreign_keys = ON;")
        
        # Read the schema file
        with open(Config.SCHEMA_PATH, 'r') as f:
            schema_sql = f.read()
            
        # Execute the schema script to create tables
        conn.executescript(schema_sql)
        conn.commit()
        
        print("Database schema created successfully.")
        
    except sqlite3.Error as e:
        print(f"An error occurred while setting up the database: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    init_db()
