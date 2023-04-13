# Lê os dois vetores com 10 elementos cada
vetor1 = []
vetor2 = []
for i in range(10):
    valor1 = int(input("Digite o valor %d do primeiro vetor: " % (i+1)))
    valor2 = int(input("Digite o valor %d do segundo vetor: " % (i+1)))
    vetor1.append(valor1)
    vetor2.append(valor2)

# Gera o terceiro vetor com os valores intercalados
vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

# Imprime o terceiro vetor
print("Terceiro vetor intercalado: ", vetor3)