from os import system
from dados import disciplinas, turmas
import sys

from utils import safe_input

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

    old_nome = disciplinas[indice]
    disciplinas[indice] = nome

    for turma in turmas:
        for aluno in turma.alunos:
            if old_nome in aluno.notas:
                aluno.notas[nome] = aluno.notas[old_nome]
                del aluno.notas[old_nome]

def listar_disciplinas():
    if disciplinas_vazia(): return

    print('Disciplinas:')
    print(disciplinas)

def selecionar_disciplina(impressao = listar_disciplinas):
    if disciplinas_vazia(): return

    impressao()

    indice = safe_input('Indique a disciplina: ', int, -1) - 1

    while indice < 0 or indice >= len(disciplinas):
        indice = safe_input('Indique a disciplina: ', int, -1) - 1

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

    indice = safe_input("\nQual a disciplina quer deletar as informações? ", int, -1) - 1


    if indice < 0 or indice >= len(disciplinas):
        print("Erro! Digite uma opção válida")
    else:
        nome = disciplinas[indice]
        del disciplinas[indice]
    
    for turma in turmas:
        for aluno in turma.alunos:
            if nome in aluno.notas:
                del aluno.notas[nome]

    print("\nNova lista disciplinas: \n")
    listar_disciplinas()

def guardar_alteracoes():
    guardar_alteracoes = input("Guardar alterações (s/n)? ").lower() == 's'

    if guardar_alteracoes:
        disciplinas.salvar()