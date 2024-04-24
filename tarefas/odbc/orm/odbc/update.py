import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('SERVER')
port = os.getenv('PORT')
database = os.getenv('DATABASE')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

def atualizar_lider_do_projeto():
    conn = None
    try:
        conn = pyodbc.connect(
            driver='{PostgreSQL Unicode}',
            server=server,
            port=port,
            database=database,
            uid=username,
            pwd=password
        )
        
        cursor = conn.cursor()
        
        sql_update = """
        UPDATE projeto
        SET responsavel = 2 
        WHERE codigo = 1;
        """
        cursor.execute(sql_update)

        conn.commit()
        print("Líder do projeto atualizado com sucesso!")
        
    except pyodbc.Error as ex:
        print(f"Ops! Ocorreu um erro ao atualizar o líder do projeto: {ex}")
        
    finally:
        if 'conn' in locals() and conn is not None:
            conn.close()

if __name__ == "__main__":
    atualizar_lider_do_projeto()
