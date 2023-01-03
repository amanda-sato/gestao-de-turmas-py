from os import system
from dados import disciplinas
import sys

def menu_disciplinas():
    opcao = ""
    while opcao != "0":
        print("\n*******************************")
        print("Menu disciplinas:\n")
        print("1) Adicionar Disciplina")
        print("2) Editar Disciplina")
        print("3) Remover Disciplina")
        print("4) Listar Disciplinas")
        print("5) Salvar Alterações")
        print("6) Retornar ao menu de turmas")
        print("0) Encerrar programa")
        print("*******************************")

        opcao = input("\nOpção: ")
        system("cls")

        if opcao == "1":
            listar_disciplinas()
            add_disciplina()
        elif opcao == "2":
            editar_disciplina()
        elif opcao == "3":
            remove_disciplina()
        elif opcao == "4":
            listar_disciplinas()
        elif opcao == "5":
            disciplinas.salvar()
        elif opcao == "6":
            guardar_alteracoes()
            return
        elif opcao == "0":
            guardar_alteracoes()
            sys.exit()
        else:
            print("ERRO!!! Escolha uma opção válida")

def add_disciplina():
    nome = input("Digite um nome para a disciplina: ")

    disciplinas.add(nome)

def editar_disciplina():
    if disciplinas_vazia(): return

    indice = selecionar_disciplina()
    nome = input("Indique o nome da disciplina: ")

    disciplinas[indice] = nome


def listar_disciplinas():
    if disciplinas_vazia(): return

    print('Disciplinas:')
    print(disciplinas)

def selecionar_disciplina(impressao = listar_disciplinas):
    if disciplinas_vazia(): return

    impressao()

    indice = int(input('Indique a disciplina: ')) - 1

    while indice < 0 or indice >= len(disciplinas):
        indice = int(input('Indique a disciplina: ')) - 1

    return indice



def disciplinas_vazia():
    if len(disciplinas) <= 0:
        print('Nenhuma disciplina cadastrada.')
        return True

    return False

def carregar_disciplinas():
    disciplinas.carregar()

def remove_disciplina():
    listar_disciplinas()

    indice = int(input("\nQual a disciplina quer deletar as informações? ")) -1

    if indice < 0 or indice >= len(disciplinas):
        print("Erro! Digite uma opção válida")
    else:
        del disciplinas[indice]

    print("\nNova lista de alunos: \n")
    listar_disciplinas()

def guardar_alteracoes():
    guardar_alteracoes = input("Guardar alterações (s/n)? ").lower() == 's'

    if guardar_alteracoes:
        disciplinas.salvar()