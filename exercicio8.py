idades = []
alturas = []

for i in range(5):
    print(f"Informe a idade da {i+1}ª pessoa:")
    idade = int(input())
    idades.append(idade)
    
    print(f"Informe a altura da {i+1}ª pessoa em metros:")
    altura = float(input())
    alturas.append(altura)

print("\nIdades e alturas em ordem inversa:\n")

for i in range(4, -1, -1):
    print(f"Idade da {5-i}ª pessoa: {idades[i]} anos")
    print(f"Altura da {5-i}ª pessoa: {alturas[i]:.2f} metros\n")