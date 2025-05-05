import psycopg2

def get_db_connection():
    return psycopg2.connect(
        dbname = "UdemyCourse",
        user = "postgres",
        password = "123456",
        host = "localhost"
)