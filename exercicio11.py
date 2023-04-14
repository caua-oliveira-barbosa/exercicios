# Lê os dois vetores com 10 elementos cada
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(10):
    valor1 = str(input("Digite o valor %d do primeiro vetor: " % (i+1)))
    valor2 = str(input("Digite o valor %d do segundo vetor: " % (i+1)))
    valor3 = str(input("Digite o valor %d do terceiro vetor: " % (i+1)))
    vetor1.append(valor1)
    vetor2.append(valor2)
    vetor3.append(valor3)

# Gera o terceiro vetor com os valores intercalados
vetor4 = []
for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

# Imprime o terceiro vetor
print("Terceiro vetor intercalado: ", vetor3)