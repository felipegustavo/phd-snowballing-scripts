import psycopg2

def connect():
    print("Conectando no banco de dados")
    return psycopg2.connect(
        dbname="doutorado_snowballing_pm",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
