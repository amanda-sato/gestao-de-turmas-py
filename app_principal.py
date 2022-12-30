from os import system
from menu_disciplina import carregar_disciplinas, menu_disciplinas
from menu_turma import carregar_turmas, menu_turma


def main():
    carregar_turmas()
    carregar_disciplinas()

    opcao = ""
    while opcao != "0":
        print("\n*******************************")
        print("Menu")
        print("1) Administrar Turmas")
        print("2) Administrar Disciplinas")
        print("0) Sair")
        print("*******************************")

        opcao = input("\nOpção: ")
        system('cls')

        if opcao == "1":
            menu_turma()
        elif opcao == "2":
            menu_disciplinas()
        elif opcao == "0":
            return
        else:
            print("ERRO!!! Escolha uma opção válida")

if __name__ == '__main__':
    main()

