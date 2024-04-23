from pony.orm import *
from datetime import date
from models import Projeto, Atividade

@db_session
def adicionar_nova_atividade():
    try:
        projeto_existente = Projeto[1]

        nova_atividade = Atividade(
            descricao='Nova tarefa importante',
            projeto=projeto_existente,
            data_inicio=date(2024, 4, 21),
            data_fim=date(2024, 4, 30)
        )
        commit()
        print("Nova tarefa adicionada com sucesso!")
    except Exception as ex:
        print(f"Ops! Ocorreu um erro ao adicionar a nova tarefa: {ex}")

if __name__ == "__main__":
    adicionar_nova_atividade()
