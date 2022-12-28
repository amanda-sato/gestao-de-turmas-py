import os

from aluno import Aluno

class Turma:
    CAMINHO = 'turmas'

    def __init__(self, id_turma, alunos = None):
        self.id_turma = id_turma

        if alunos is None:
            self.alunos = []
        else:
            self.alunos = alunos

    def add(self, aluno):
        aluno.matricula = '#'.join(f'{self.id_turma[:5]:05}'.upper().split() + [f'{len(self.alunos) + 1:03}'])

        self.alunos.append(aluno)

    def delet(self, indice):
        self.alunos.pop(indice)

    def edit(self, indice, aluno):
        self.alunos[indice] = aluno

    def get_aluno(self, indice):
        return self.alunos[indice]

    def mostrar(self):
        for i, aluno in enumerate(self.alunos):
            print(i + 1, '-', aluno)

    def salvar(self):
        f = open(self.ficheiro, "w", encoding="utf-8")

        for p in self.alunos:
            f.write(p.str_ficheiro())

        f.close()

    @property # Faz com que o método possa ser chamado como se um atributo fosse.
    def ficheiro(self):
        return f"{Turma.CAMINHO}/{self.id_turma}.txt"

    def carregar(self):
        if os.path.isfile(self.ficheiro):
            f = open(self.ficheiro, "r", encoding="utf-8") #define a formatação de como o python vai interpretar os bytes do arquivo.
            linha = f.readline()

            while linha != "":
                nome, genero, matricula, notas = linha.strip().split(" | ")
                self.add(Aluno(nome, genero, matricula, eval(notas)))
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

