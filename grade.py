import os

class Grade:
    CAMINHO = "grades" #constante de classe

    def __init__(self, id, disciplinas = None):
        self.id = id

        if disciplinas is None:
            self.disciplinas = []
        else:
            self.disciplinas = list(disciplinas)

    def add(self, disciplina):
        self.disciplinas.append(disciplina)

    def salvar(self):
        f = open(self.ficheiro, "w", encoding="utf-8")

        for d in self.disciplinas: f.write(f"{d}\n")

        f.close()

    def carregar(self):
        if os.path.isfile(self.ficheiro):
            f = open(self.ficheiro, "r", encoding="utf-8") #define a formatação de como o python vai interpretar os bytes do arquivo.
            linha = f.readline()

            while linha != "":
                nome  = linha.strip()
                self.add(nome)
                linha = f.readline()

            f.close()

    @property # faz com que o método possa ser acessado como se propriedade fosse.
    def ficheiro(self):
        return f"{Grade.CAMINHO}/{self.id}.txt"

    def __setitem__(self, indice, disciplina):
        self.disciplinas[indice] = disciplina

    def __getitem__(self, indice):
        return self.disciplinas[indice]

    def __len__(self):
        return len(self.disciplinas)

    def __str__(self):
        lista = []

        # Gera lista de disciplinas.
        # enumerate gera uma lista de tuplas, cada uma com dois elementos
        # exemplo:
        # [(0, 'Matemática'), ..., (5, 'História')]
        # 
        for indice, disciplina in enumerate(self.disciplinas):
            lista += [f"{indice + 1} - {disciplina}"]

        # Gera uma string com todos os elementos de lista, 
        # concatenados e separados por '\n'
        return "\n".join(lista)

    def __repr__(self):
        return f"Disciplina(id={self.id}, disciplinas={self.disciplinas})"

    def __delitem__(self, indice):
        del self.disciplinas[indice]

