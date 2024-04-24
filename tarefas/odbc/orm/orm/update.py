from pony.orm import *
from models import Projeto, Funcionario

def atualizar_responsavel_do_projeto():
    try:
        with db_session:
            projeto = Projeto[1]
            novo_resp = Funcionario[1]
            projeto.responsavel = novo_resp
            commit()
            print("Responsável pelo projeto atualizado com sucesso!")
    except Exception as ex:
        print(f"Ops! Ocorreu um erro ao atualizar o responsável pelo projeto: {ex}")

if __name__ == "__main__":
    atualizar_responsavel_do_projeto()
