# ================================
# PIM II - NotaFlow (Python)
# Universidade Paulista - UNIP
# Autor(es): Gabriel Mazzaron
# ================================

from collections import deque

# ===========================
# Menu principal
# ===========================

def menu():
    discipinas = ["Português", "Matemática", "História", "Filosofia", "Sociologia", "Geografia", "Biologia", "Química", "Física", "Inglês", "Educação Física"]

    while True:
        print("\n=== NotaFlow ===")
        print("Escolha a disciplina para cadastro:")
        for i, disc in enumerate(discipinas, start=1):
            print(f"{i}. {disc}")
        print("0. Sair")

        opcao = input("Opção: ")

        if opcao == "0":
            print("\nEncerrando o sistema")
            break
        elif opcao.isdigit() and 1 <= int(opcao) <= len(discipinas):
            disciplina = discipinas[int(opcao) - 1]
            cadastro(disciplina)
        else:
            print("Opção inválida. Tente Novamente.")

# ===========================
# Cadastro de Alunos
# ===========================

def cal_media(notas):
    return sum(notas) / len(notas)

def cadastro(disciplina):
    fila = Fila()
    print(f"\n=== Cadastro de Aluno - {disciplina.upper()} ===")

    while True:
        nome = input("Nome do Aluno: ").strip()
        ra = input("RA: ").strip()
        turma = input("Turma: ").strip()

        notas = []
        for i in range(1, 5):
            nota = float(input(f"Digite a nota {i}: "))
            notas.append(nota)
        
        media = cal_media(notas)
        aluno = {
            "Nome": nome,
            "RA": ra,
            "Turma": turma,
            "Notas": notas,
            "Média": media
        }

        fila.add(aluno)
        print(f"\nAluno {nome} cadastrado\nCom média de {media}")

        continuar = input("\nDeseja cadastrar outro aluno (s/n)").lower()
        if continuar != 's':
            break

    fila.salvar(disciplina)
    return fila

# ===========================
# Estrutura de fila
# ===========================

class Fila:
    def __init__(self):
        self.fila = deque()

    def add(self, aluno):
        self.fila.append(aluno)

    def lista(self):
        for a in self.fila:
            print(a)

    def salvar(self, disciplina):
        nome_arquivo = f"{disciplina}.txt"
        with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
            for a in self.fila:
                arquivo.write(f"Nome: {a['Nome']}, RA: {a['RA']}, Turma: {a['Turma']}, Notas: {a['Notas']}, Média: {a['Média']:.2f}\n")
                print(f"Salvo em {nome_arquivo} com sucesso!\n")

# ===========================
# Execução do código
# ===========================

if __name__ == "__main__":
    menu()