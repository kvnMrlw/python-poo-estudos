from rich import print, inspect

class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade


    def fazer_aniverasario(self):
        self.idade += 1

    
class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula():
        pass


class Professor(Pessoa):
    def __init__(self, nome="", idade=0, especialidade="", nivel=""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    
    def dar_aula():
        pass


class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = cargo 
        self.setor = setor 

    
    def bater_ponto():
        pass
  


aluno = Aluno("josé", 17, "ads", "ads01")
inspect(aluno, methods= True)