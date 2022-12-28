class Aluno:
    def __init__(self, nome, genero, matricula = '', notas = None):
        self.nome = nome
        self.genero = genero
        self.matricula = matricula

        if notas is None:
            self.notas = {}
        else:
            self.notas = notas

    def add_nota(self, disciplina, nota):
        self.notas[disciplina] = nota

    def rm_nota(self, disciplina):
        del self.notas[disciplina]

    def imprimir_notas(self, grade = None):
        disciplinas = self.notas.keys() if grade is None else grade

        print("{:<12} {:>4}".format("Disciplinas", "Notas"))
        print("{:<12} {:>4}".format("-----", "----"))

        for disciplina in disciplinas:
            nota = self.notas.get(disciplina, '')

            if isinstance(nota, str):
                str_nota = f"{nota:>4}"
            else:
                str_nota = f"{nota:>4.2f}"

            print(f"{disciplina:<12} {str_nota}")

    def __str__(self):
        return f'{self.nome}, {self.genero}, {self.matricula}'

    # Retorna a representação de um objeto como string
    # >>> aluno = Aluno('Max', 'M', '0001')
    # >>> repr(alunuo)
    # Aluno('Max', 'M', '0001')
    # >>> aluno
    # Aluno('Max', 'M', '0001')
    def __repr__(self):
        return f"Aluno({self.nome}, {self.genero}, {self.matricula})"

    def str_ficheiro(self):
        return self.nome + " | " + self.genero + " | " + str(self.matricula) + " | " + repr(self.notas) + "\n"

