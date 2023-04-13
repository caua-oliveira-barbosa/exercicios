# cria um vetor vazio de tamanho 5
vetor = [0] * 5

# faz a leitura dos números do vetor
for i in range(5):
    vetor[i] = int(input("Digite o número {}: ".format(i+1)))

# calcula a soma e a multiplicação dos números do vetor
soma = sum(vetor)
multiplicacao = 1
for num in vetor:
    multiplicacao *= num

# exibe os resultados
print("Números do vetor:", vetor)
print("Soma dos números:", soma)
print("Multiplicação dos números:", multiplicacao)