# criar um vetor para armazenar as médias dos alunos
medias = []

# iterar sobre cada aluno
for i in range(1, 11):
    # solicitar as notas do aluno
    print(f"Informe as notas do aluno {i}:")
    nota1 = str(input("Nota 1: "))
    nota2 = str(input("Nota 2: "))
    nota3 = str(input("Nota 3: "))
    nota4 = str(input("Nota 4: "))
    
    # calcular a média do aluno e adicionar ao vetor de médias
    media = sum(medias) / 4
    medias.append(media)

# contar o número de alunos com média maior ou igual a 7.0
num_alunos_aprovados = 0
for media in medias:
    if media >= 7.0:
        num_alunos_aprovados += 1

# imprimir o número de alunos aprovados
print(f"O número de alunos com média maior ou igual a 7.0 é: {num_alunos_aprovados}")