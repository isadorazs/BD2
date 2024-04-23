import pyodbc
from dotenv import load_dotenv
import os

def establish_database_connection():
    load_dotenv()

    server = os.getenv('SERVER')
    port = os.getenv('PORT')
    database = os.getenv('DATABASE')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    try:
        conn = pyodbc.connect(
            driver='{PostgreSQL Unicode}',
            server=server,
            port=port,
            database=database,
            uid=username,
            pwd=password
        )
        print("Conexão bem-sucedida!")
        return conn
    except pyodbc.Error as ex:
        print(f"Erro ao conectar ao banco de dados: {ex}")
        return None

def main():
    conn = establish_database_connection()
    if conn:
        conn.close()

if __name__ == "__main__":
    main()
