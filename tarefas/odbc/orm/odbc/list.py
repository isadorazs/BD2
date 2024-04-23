import pyodbc
from dotenv import load_dotenv
import os

def connect_to_database():
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
        return conn
    except pyodbc.Error as ex:
        print(f"Erro ao conectar ao banco de dados: {ex}")
        return None

def fetch_and_print_activities(conn):
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projeto;")
        projects = cursor.fetchall()

        for project in projects:
            print(f"Atividades do projeto '{project[1]}':")
            
            cursor.execute(f"SELECT * FROM atividade WHERE projeto = {project[0]};")
            activities = cursor.fetchall()

            for activity in activities:
                print(f"- {activity[1]}")

            print()
    except pyodbc.Error as ex:
        print(f"Erro ao executar consulta SQL: {ex}")
    finally:
        conn.close()

def main():
    conn = connect_to_database()
    fetch_and_print_activities(conn)

if __name__ == "__main__":
    main()
