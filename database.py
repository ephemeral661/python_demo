import sqlite3

DATABASE_NAME = "investment_data.db"


# Initialize the database and table.
def init_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        # Create a Trades table with trade_id, security_name, amount, date, issuer, and corporate_action
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Trades (
                id INTEGER PRIMARY KEY,
                trade_id TEXT NOT NULL,
                security_name TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                issuer TEXT NOT NULL,
                corporate_action TEXT
            )
        """)
