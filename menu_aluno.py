from os import system
import sys
from aluno import Aluno
from menu_disciplina import selecionar_disciplina
from menu_disciplina import disciplinas
from utils import safe_input

def menu_alunos(turma):
    opcao = ""
    while opcao != "0":

        print("\n*******************************")
        print(f"Menu turma {turma.id_turma}\n")
        print("1) Adicionar Aluno")
        print("2) Remover Aluno")
        print("3) Mostrar lista de alunos")
        print("4) Editar Aluno")
        print("5) Administrar notas")
        print("6) Retornar ao menu de turmas")
        print("0) Encerrar programa")
        print("*******************************")

        opcao = input("\nOpção: ")
        system("cls")

        if opcao == "1":
            add_aluno(turma)
        elif opcao == "2":
            remove_aluno(turma)
        elif opcao == "3":
            turma.mostrar()
        elif opcao == "4":
            editar_aluno(turma)
        elif opcao == "5":
            turma.mostrar()
            indice = safe_input("\nIndique o aluno? ", int, -1) - 1

            if indice < 0 or indice > len(turma.alunos):
                print("ERRO!!! Escolha uma opção válida")
            else:
                aluno = turma.get_aluno(indice)
                menu_notas(aluno)
        elif opcao == "6":
            guardar_alteracoes = input("Guardar alterações (s/n)? ").lower() == 's'

            if guardar_alteracoes:
                turma.salvar()
            return
        elif opcao == "0":
            guardar_alteracoes = input("Guardar alterações (s/n)? ").lower() == 's'

            if guardar_alteracoes:
                turma.salvar()

            sys.exit()

        else:
            print("ERRO!!! Escolha uma opção válida")

def add_aluno(turma):
    print("Lista de alunos atual: \n")
    turma.mostrar()

    print("\nInsira informações do novo aluno: \n")
    n = input("Nome: ")
    g = informar_genero()

    turma.add(Aluno(n, g))

    print("\nNova lista de alunos: \n")
    turma.mostrar()

def remove_aluno(turma):
    turma.mostrar()

    indice = safe_input("\nQual o aluno quer deletar as informações? ", int, -1) - 1

    if indice < 0 or indice >= len(turma.alunos):
        print("Erro! Digite uma opção válida")
    else:
        turma.delet(indice)

    print("\nNova lista de alunos: \n")
    turma.mostrar()

def editar_aluno(turma):
    turma.mostrar()

    indice = safe_input("\nQual o aluno quer editar as informações? ", int, -1) - 1
    old_aluno = turma.get_aluno(indice)

    if indice < 0 or indice >= len(turma.alunos):
        print("Erro! Digite uma opção válida")
    else:
        print("Insira as novas informações do aluno: \n")
        n = input("Nome: ")
        g = informar_genero()

        turma.edit(indice, Aluno(n, g, old_aluno.matricula, old_aluno.notas))

        print("\nNova lista de alunos: \n")
        turma.mostrar()

def informar_genero():
    g = input("Gênero (F/M): ")

    while g.upper() not in ('F', 'M'):
        g = input("Gênero (F/M): ")

    return g

def menu_notas(aluno):
    opcao = ""
    while opcao != "0":
        print("\n*******************************")
        print(f"Menu {aluno.nome}: \n")
        print("1) Adicionar Nota")
        print("2) Editar Nota")
        print("3) Listar notas")
        print("0) Retornar ao menu de alunos")
        print("*******************************")

        opcao = input("\nOpção:")
        system("cls")

        if opcao == "1":
            informar_nota(aluno)
        elif opcao == "2":
            informar_nota(aluno) #A função de adição é a mesma de inclusão, então foi repetida
        elif opcao == "3":
            aluno.imprimir_notas(disciplinas)
        elif opcao == "0":
            return
        else:
            print("ERRO!!! Escolha uma opção válida")

def informar_nota(aluno):
    indice = selecionar_disciplina(lambda: aluno.imprimir_notas(disciplinas))

    nota = safe_input("Indique a nota: ", float, -1)

    while nota < 0 or nota > 20:
        nota = safe_input("Indique a nota: ", float, -1)

    aluno.add_nota(disciplinas[indice], nota)