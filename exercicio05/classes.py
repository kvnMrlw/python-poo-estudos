from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade


    def fazer_aniverasario(self):
        self.idade += 1

    @abstractmethod
    def estudar (self):
        pass
    
class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        pass

    def estudar(self):
        return super().estudar()

class Professor(Pessoa):
    def __init__(self, nome="", idade=0, especialidade="", nivel=""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    
    def dar_aula(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = cargo 
        self.setor = setor 

    
    def bater_ponto(self):
        pass
  
