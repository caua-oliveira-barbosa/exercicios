A = [] # criando uma lista vazia para armazenar os números do vetor

# lendo os valores do vetor
for i in range(10):
    num = int(input("Digite um número inteiro para o vetor A: "))
    A.append(num)

# calculando a soma dos quadrados dos elementos do vetor
soma_quadrados = 0
for num in A:
    soma_quadrados += num**2

# mostrando o resultado na tela
print("A soma dos quadrados dos elementos do vetor A é:", soma_quadrados)