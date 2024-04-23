import pyodbc
from dotenv import load_dotenv
import os

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
    
    cursor = conn.cursor()
    
    # Adiciona uma nova atividade
    insert_query = """
    INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
    VALUES ('Nova tarefa importante', 2, '2024-04-25', '2024-04-30')
    """

    cursor.execute(insert_query)

    conn.commit()
    print("Nova tarefa adicionada com sucesso!")
    
except pyodbc.Error as ex:
    print(f"Ops! Encontrei um erro ao conectar ou executar comandos SQL: {ex}")
    
finally:
    if conn:
        conn.close()
