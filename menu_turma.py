import glob
import os
from os import system
from menu_aluno import menu_alunos
from menu_disciplina import relacao_de_aprovados
from turma import Turma

turmas = []
turmas_deletadas = []

def menu_turma():
    opcao = ""

    while opcao != "0":
        print("\n*******************************")
        print("Menu Turmas: \n")
        print("1) Adicionar Turma")
        print("2) Remover Turma")
        print("3) Listar turmas")
        print("4) Editar Turma ")
        print("5) Relação de alunos aprovados e reprovados")
        print("6) Média geral por aluno")
        print("7) Administrar alunos")
        print("8) Salvar alterações")
        print("0) Sair")
        print("*******************************")

        opcao = input("\nOpção: ")
        system('cls')

        if opcao == "1":
            add_turma()
        elif opcao == "2":
            remove_turma()
        elif opcao == "3":
            listar_turmas()
        elif opcao == "4":
            editar_turma()
        elif opcao == "5":
            relacao_de_aprovados(turmas)
        elif opcao == "6":
            media_geral_por_aluno()
        elif opcao == "7" and not turmas_vazia():
            indice = selecionar_turma()
            menu_alunos(turmas[indice])
        elif opcao == "8":
            salvar_turmas()
        elif opcao == "0":
            guardar_alteracoes = input("Guardar alterações (s/n)? ").lower() == 's'

            if guardar_alteracoes:
                salvar_turmas()

            return
        else:
            print("ERRO!!! Escolha uma opção válida")

def add_turma():
    id_turma = input("Digite o nome da turma: ")
    turmas.append(Turma(id_turma))

def remove_turma():
    if turmas_vazia(): return

    indice = selecionar_turma()
    turmas_deletadas.append(Turma(turmas[indice].id_turma))
    turmas.pop(indice)

def listar_turmas():
    if turmas_vazia(): return

    print('Turmas:')

    for indice, turma in enumerate(turmas):
        print(indice + 1, '-', turma)

def editar_turma():
    if turmas_vazia(): return

    indice = selecionar_turma()

    id_turma = input('Indique o novo nome da turma: ')

    old_id_turma = turmas[indice].id_turma

    if id_turma != old_id_turma:
        # Fica mais fácil remover a turma a partir de uma instância da própria classe Turma.
        # já que ela contém métodos e propriedades que "sabem" onde uma Turma é salva.
        turmas_deletadas.append(Turma(old_id_turma))

    turmas[indice].id_turma = id_turma

def carregar_turmas():
    for ficheiro in glob.glob(f'{Turma.CAMINHO}/*.txt'):
        id_turma = os.path.basename(ficheiro).rstrip('.txt')

        turma = Turma(id_turma)
        turma.carregar()

        indice = indice_de(id_turma)

        if indice < 0:
            turmas.append(turma)
        else:
            turmas[indice] = turma

def salvar_turmas():
    for turma in turmas:
        turma.salvar()

    for turma_deletada in turmas_deletadas:
        turma_deletada.deletar()

def indice_de(id_turma):
    for indice, turma in enumerate(turmas):
        if turma.id_turma == id_turma:
            return indice

    return -1

def selecionar_turma():
    if turmas_vazia(): return

    listar_turmas()

    indice = int(input('Indique a turma: ')) - 1

    return indice

def turmas_vazia():
    if len(turmas) <= 0:
        print('Nenhuma turma cadastrada.')
        return True

    return False

def media_geral_por_aluno():
    print(f"{'Turma':<8} {'Aluno':>17} {'M. Geral':>10}")
    print(f"{'---':<8} {'---':>17} {'---':>10}")

    for turma in turmas:
        for aluno in turma.alunos:
            if aluno.media_geral() < 0:
                media = f"{'':>10}"
            else:
                media = f"{aluno.media_geral():>10.2f}"
            
            print(f"{turma.id_turma:<8} {aluno.nome:>17} {media}")