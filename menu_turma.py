import glob
import os
from os import system
from aluno import Aluno
from menu_aluno import menu_alunos
from turma import Turma
from dados import turmas, turmas_deletadas, disciplinas
import sys

from utils import safe_input, trunca

def menu_turma():
    opcao = ""

    while opcao != "0":
        print("\n*******************************")
        print("Menu Turmas: \n")
        print("1)  Adicionar Turma")
        print("2)  Remover Turma")
        print("3)  Listar turmas")
        print("4)  Editar Turma ")
        print("5)  Relação de alunos aprovados e reprovados")
        print("6)  Média geral por aluno")
        print("7)  Taxa de aprovação por disciplina")
        print("8)  Administrar alunos")
        print("9)  Salvar alterações")
        print("10) Retornar ao menu anterior")
        print("0)  Encerrar programa")
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
            relacao_de_aprovados()
        elif opcao == "6":
            media_geral_por_aluno()
        elif opcao == "7":
            taxa_de_aprovacao()
        elif opcao == "8" and not turmas_vazia():
            indice = selecionar_turma()
            menu_alunos(turmas[indice])
        elif opcao == "9":
            salvar_turmas()
        elif opcao == "10":
            guardar_alteracoes()
            return
        elif opcao == "0":
            guardar_alteracoes()
            sys.exit()
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

    indice = safe_input('Indique a turma: ', int, -1) - 1

    while indice < 0 or indice >= len(turmas):
        indice = safe_input('Indique a turma: ', int, -1) - 1

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

            print(f"{trunca(turma.id_turma, 8):<8} {trunca(aluno.nome, 17):>17} {media}")

def relacao_de_aprovados():
    formato = '{:<12} {:>12} {:>20} {:>12}'

    print(formato.format('Disciplina', 'Turma', 'Aluno', 'Situação'))

    for disciplina in disciplinas:
        for turma in turmas:
            for aluno in turma.alunos:
                print(formato.format(
                    disciplina,
                    turma.id_turma,
                    aluno.nome,
                    aluno.fancy_situacao(disciplina)
                ))

def taxa_de_aprovacao():
    print(f"{'Disciplina':<15} {'% aprovados':>15} {'% reprovados':>15} {'% não informados':>15}")
    print(f"{'----':<15} {'----':>15} {'----':>15} {'----':>15}")

    for disciplina in disciplinas:
        sumario = {
            Aluno.SEM_DADOS: 0,
            Aluno.APROVADO: 0,
            Aluno.REPROVADO: 0,
        }

        total = 0

        for turma in turmas:
            total += len(turma.alunos)

            for aluno in turma.alunos:
                sumario[aluno.situacao(disciplina)] += 1

        for situacao, contagem in sumario.items():
            sumario[situacao] = contagem / total

        print(f"{trunca(disciplina, 15):<15} {sumario[Aluno.APROVADO]:>15.2%} {sumario[Aluno.REPROVADO]:>15.2%} {sumario[Aluno.SEM_DADOS]:>15.2%}")

def guardar_alteracoes():
    guardar_alteracoes = input("Guardar alterações (s/n)? ").lower() == 's'

    if guardar_alteracoes:
        salvar_turmas()