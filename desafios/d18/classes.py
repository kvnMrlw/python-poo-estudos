from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome, nasc):
        self._nome = nome
        self._nasc = nasc


    @property
    def idade(self):
        return date.today().year - self._nasc

    @idade.setter
    def idade(self, idade):
        raise PermissionError("Você não pode alterar idade, tente mudar o ano de nascimento")

    @property
    def nascimento(self):
        return self._nasc

    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= self.nascimento:
            self._nasc = ano
        else:
            raise ValueError ("Ano de nascimento inválido!") 


class Aluno(Pessoa):

    cursos_oficias = ["ADM", "ADS", "ENGE", "ODONTO"]

    def __init__(self, nome, nasc, curso):
        super().__init__(nome, nasc)
        self._curso = curso


    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficias:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError (f"O curso {curso} não esta nos nossos cursos")


    def add_cursio(self, curso):
        curso = curso.strip().upper()
        if 3 <= len(curso) <= 5:
            Aluno.cursos_oficias.append(curso)
        else:
            raise ValueError ("O nome do curso deve ter apenas entre 3 a 5 letras")
