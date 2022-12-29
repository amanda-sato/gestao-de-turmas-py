from os import system
from grade import Grade

disciplinas = Grade(id="Disciplinas")

def menu_disciplinas():
    opcao = ""
    while opcao != "0":
        print("\n*******************************")
        print("Menu disciplinas:\n")
        print("1) Adicionar Disciplina")
        print("2) Editar Disciplina")
        print("2) Remover Disciplina")
        print("3) Listar Disciplinas")
        print("4) Salvar Alterações")
        print("0) Retonar ao menu de turmas")
        print("*******************************")

        opcao = input("\nOpção: ")
        system("cls")

        if opcao == "1":
            add_disciplina()
        elif opcao == "2":
            editar_disciplina()
        elif opcao == "3":
            listar_disciplinas()
        elif opcao == "4":
            disciplinas.salvar()
        elif opcao == "0":
            guardar_alteracoes = input("Guardar alterações (s/n)? ").lower() == 's'

            if guardar_alteracoes:
                disciplinas.salvar()

            return
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

def selecionar_disciplina():
    if disciplinas_vazia(): return

    listar_disciplinas()

    indice = int(input('Indique a disciplina: ')) - 1

    return indice

def listar_disciplinas():
    if disciplinas_vazia(): return

    print('Disciplinas:')
    print(disciplinas)

def disciplinas_vazia():
    if len(disciplinas) <= 0:
        print('Nenhuma disciplina cadastrada.')
        return True

    return False

def carregar_disciplinas():
    disciplinas.carregar()

def relacao_de_aprovados(turmas):
    formato = '{:<12} {:>12} {:>20} {:>12}'

    print(formato.format('Disciplina', 'Turma', 'Aluno', 'Situação'))

    for disciplina in disciplinas:
        for turma in turmas:
            for aluno in turma.alunos:
                print(formato.format(
                    disciplina,
                    turma.id_turma,
                    aluno.nome,
                    aluno.situacao(disciplina)
                ))