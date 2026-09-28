from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplina = {}

    def matricular(self, disciplina: Disciplina):
        """Adicionar a disciplina a lista de disciplina vinculada ao aluno"""
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        """Adicionar a nota do aluno no dict referente a 1 disciplina"""
        if disciplina.nome not in self.notas_por_disciplina:
            self.matricular(disciplina)
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def media_por_d(self, d: Disciplina):
        notas = self.notas_por_disciplina.get(d.nome, [])
        if not notas:
            return 0.0
        return sum(notas) / len(notas)

    def media_geral(self):
        medias_por_disciplina = []
        for d in self.disciplinas:
            media_d = self.media_por_d(d)
            medias_por_disciplina.append(media_d)
        if not medias_por_disciplina:
            return 0.0
        return sum(medias_por_disciplina) / len(medias_por_disciplina)

    def exibir_boletim(self):
        print(f"Aluno: {self.nome} | Matricula: {self.matricula} Curso: {self.curso}")
        if not self.disciplinas:
            print("Sem disciplinas matriculada")
            return
        for i in self.disciplinas:
            i.exibir_infos()
            print(f"Notas do aluno em {i.nome}: {self.notas_por_disciplina[i.nome]}")
            print(f"Disciplina: {i.nome} | Media: {self.media_por_d(i)}")
        print(f"Media geral: {self.media_geral()}")
