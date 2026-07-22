from rich import print, inspect
from classes import Pessoa, Aluno, Professor, Funcionario



aluno = Aluno("josé", 17, "ads", "ads01")
inspect(aluno, methods= True)