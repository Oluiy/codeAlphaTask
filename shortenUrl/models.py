from db import get_db_connection

def create_table():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS urls (
                    id SERIAL PRIMARY KEY,
                    short TEXT UNIQUE NOT NULL,
                    long TEXT NOT NULL
                );
            ''')
            conn.commit()


def insert_url(short, long):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO urls (short, long) VALUES (%s, %s) RETURNING id", (short, long))
            conn.commit()
            return cur.fetchone()[0]

def get_long_url(short):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT long FROM urls WHERE short = %s", (short,))
            result = cur.fetchone()
            return result[0] if result else None
