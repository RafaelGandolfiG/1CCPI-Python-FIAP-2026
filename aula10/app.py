from aluno import Aluno
from disciplina import Disciplina

aluno1 = Aluno("Paulo", "123456", "Ciência da Computação")

# print(aluno1.nome)
# print(aluno1.matricula)
# print(aluno1.curso)
# print(aluno1.disciplinas)
# print(aluno1.notas_por_disciplina)

model_lin = Disciplina("Modelagem Linear", "Rodolfo")
dsa = Disciplina("Data Structures", "Erick")

aluno1.matricular(model_lin)
aluno1.matricular(dsa)

print(aluno1.disciplinas[0].nome)
print(aluno1.disciplinas[1].nome)

aluno1.adicionar_nota(model_lin, 10)
aluno1.adicionar_nota(model_lin, 6)
aluno1.adicionar_nota(dsa, 5)
aluno1.adicionar_nota(dsa, 4)

print(aluno1.notas_por_disciplina["Modelagem Linear"])

print(aluno1.media_por_d(model_lin))

print(aluno1.media_geral())

aluno1.exibir_boletim()