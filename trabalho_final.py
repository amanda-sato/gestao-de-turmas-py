import os
from os import system
import glob

class Turma:
    CAMINHO = 'turmas'

    def __init__(self, id_turma, alunos = None):
        self.id_turma = id_turma

        if alunos is None:
            self.alunos = []
        else:
            self.alunos = alunos

    def add(self, aluno):
        self.alunos.append(aluno)

    def delet(self, indice):
        self.alunos.pop(indice)

    def edit(self, indice, aluno):
        self.alunos[indice] = aluno

    def mostrar(self):
        for i, aluno in enumerate(self.alunos):
            print(i + 1, '-', aluno)

    def salvar(self):
        f = open(self.ficheiro, "w", encoding="utf-8")

        for p in self.alunos:
            f.write(p.str_ficheiro())

    @property # Faz com que o método possa ser chamado como se um atributo fosse.
    def ficheiro(self):
        return f"{Turma.CAMINHO}/{self.id_turma}.txt"

    def carregar(self):
        if os.path.isfile(self.ficheiro):
            f = open(self.ficheiro, "r", encoding="utf-8") #define a formatação de como o python vai interpretar os bytes do arquivo.
            linha = f.readline()

            while linha != "":
                nome, genero, matricula, media = linha.strip().split(" | ")
                self.add(Aluno(nome, genero, matricula, int(media)))
                linha = f.readline()

            f.close()

    def deletar(self):
        if os.path.isfile(self.ficheiro):
            os.remove(self.ficheiro)

    def __str__(self):
        return f'Turma {self.id_turma}'

    def __repr__(self):
        id_turma, alunos = self.id_turma, self.alunos
        return f'Turma({id_turma=}, {alunos=})'


class Aluno:
    def __init__(self, nome, genero, matricula,media):
        self.nome = nome
        self.genero = genero
        self.matricula = matricula
        self.media = media

    def __str__(self):
        return f'{self.nome}, {self.genero}, {self.matricula}, {self.media}'

    # Retorna a representação de um objeto como string
    # >>> aluno = Aluno('Max', 'M', '0001', 20)
    # >>> repr(alunuo)
    # Aluno('Max', 'M', '0001', 20)
    # >>> aluno
    # Aluno('Max', 'M', '0001', 20)
    def __repr__(self):
        return f"Aluno({self.nome}, {self.genero}, {self.matricula}, {self.media})"

    def str_ficheiro(self):
        return self.nome + " | " + self.genero + " | " + str(self.matricula) + " | " + str(self.media) + "\n"

turmas = []
turmas_deletadas = []

def main():
    carregar_turmas()
    menu_turma()

def nao_implementado():
    print("TEM QUE IMPLEMENTAR DEPOIS HEIN!")

def menu_turma():
    opcao = ""

    while opcao != "0":
        print("\n*******************************")
        print("Menu Turmas: \n")
        print("1) Adicionar Turma")
        print("2) Remover Turma")
        print("3) Listar turmas")
        print("4) Editar Turma ")
        print("5) Qual a média das notas dos alunos por Turma? ")
        print("6) Administrar alunos")
        print("7) Salvar alterações")
        print("0) Sair")
        print("*******************************")

        opcao = input("\nOpção:")

        if opcao == "1":
            add_turma()
        elif opcao == "2":
            remove_turma()
        elif opcao == "3":
            listar_turmas()
        elif opcao == "4":
            editar_turma()
        elif opcao == "5":
            nao_implementado()
        elif opcao == "6" and not turmas_vazia():
            indice = selecionar_turma()
            menu_alunos(turmas[indice])
        elif opcao == "7":
            salvar_turmas()
        elif opcao == "0":
            return
        else:
            print("ERRO!!! Escolha uma opção válida")

        input("Aperte qualquer tecla para continuar.")
        system('cls')

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

def menu_alunos(turma):
    opcao = ""
    while opcao != "0":

        print("\n*******************************")
        print("Menu " + turma.id_turma + ": \n")
        print("1) Adicionar Aluno")
        print("2) Remover Aluno")
        print("3) Mostrar lista de alunos")
        print("4) Qual aluno deseja editar as informações? ")
        print("5) Qual a média das notas dos alunos da turma? ")
        print("6) Qual a média ")
        print("0) Retornar ao menu de turmas")
        print("*******************************")

        opcao = input("\nOpção:")
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
            pass
        elif opcao == "6":
            pass
        elif opcao == "0":
            guardar_alteracoes = input("Guardar alterações (s/n)? ").lower() == 's'

            if guardar_alteracoes:
                turma.salvar()
        else:
            print("ERRO!!! Escolha uma opção válida")

def add_aluno(turma):
    print("Lista de alunos atual: \n")
    turma.mostrar()

    print("\nInsira informações do novo aluno: \n")
    n = input("Nome: ")
    g = input("Gênero (F/M): ").upper()
    mt = input("Matrícula: ")
    md = input("Média: ")

    turma.add(Aluno(n,g,mt,md))

    print("\nNova lista de alunos: \n")
    turma.mostrar()

def remove_aluno(turma):
    turma.mostrar()

    indice = int(input("\nQual o aluno quer deletar as informações? ")) -1

    if indice < 0 or indice >= len(turma.alunos):
        print("Erro! Digite uma opção válida")
    else:
        turma.delet(indice)

    print("\nNova lista de alunos: \n")
    turma.mostrar()

def editar_aluno(turma):
    turma.mostrar()

    indice = int(input("\nQual o aluno quer editar as informações? ")) -1

    if indice < 0 or indice >= len(turma.alunos):
        print("Erro! Digite uma opção válida")
    else:
        print("Insira as novas informações do aluno: \n")
        n = input("Nome: ")
        g = input("Gênero (F/M): ").upper()
        mt = input("Matrícula: ")
        md = input("Média: ")

        turma.edit(indice, Aluno(n,g,mt,md))

        print("\nNova lista de alunos: \n")
        turma.mostrar()

if __name__ == '__main__':
    main()
