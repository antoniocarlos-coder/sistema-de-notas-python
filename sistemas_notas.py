# 1. calcular a média do aluno
def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

# 2. Condição Aprovado,Recuperação ou Reprovado
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

# 3. Cadastro Aluno perguntar nome e notas do aluno (While)
alunos = []
continuar = "s"
while continuar == "s":

    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota do primeiro bimestre: "))
    while nota1 <0 or nota1 > 10:
        print("Nota do primeiro bimestre invalida!")
        nota1 = float(input("Digite a nota do primeiro bimestre: "))

    nota2 = float(input("Digite a nota do segundo bimestre: "))
    while nota2 < 0 or nota2 > 10:
        print("Nota do segundo bimestre invalida!")
        nota2 = float(input("Digite a nota do segundo bimestre: "))

    nota3 = float(input("Digite a nota do terceiro bimestre: "))
    while nota3 <0 or nota3 > 10:
        print("Nota do terceiro bimestre invalida!")
        nota3 = float(input("Digite a nota do terceiro bimestre: "))

    nota4 = float(input("Digite a nota do quarto bimestre: "))
    while nota4 <0 or nota4 > 10:
        print("Nota do quarto bimestre invalida!")
        nota4 = float(input("Digite a nota do quarto bimestre: "))
    alunos.append({
        "Nome": nome,
        "Nota1": nota1,
        "Nota2": nota2,
        "Nota3": nota3,
        "Nota4": nota4
    })
    continuar = input("Deseja continuar? [S/N] ").lower()


# Pesquisar aluno
nome_pesquisado = input("Pesquisar nome do aluno: ")

encontrado = False

for aluno in alunos:
    if aluno["Nome"].lower() == nome_pesquisado.lower():
        encontrado = True
        print("=" * 12)
        print("Aluno:", aluno["Nome"])
        print("Nota 1º BI:", aluno["Nota1"])
        print("Nota 2º BI:", aluno["Nota2"])
        print("Nota 3º BI:", aluno["Nota3"])
        print("Nota 4º BI:", aluno["Nota4"])

        media = calcular_media(
            aluno["Nota1"],
            aluno["Nota2"],
            aluno["Nota3"],
            aluno["Nota4"]
        )

        print("Média:", media)
        print("Situação:", verificar_situacao(media))
        print("=" * 12)
if encontrado == False:
    print("Aluno não encontrado!")