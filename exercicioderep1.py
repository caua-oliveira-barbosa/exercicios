#Lista para inserir as notas
nota = input("Digite uma nota de 0 a 10: ")
parada = False

#Comando para definir que as notas só podem ser de 0 a 10
while parada==False:
    nota1 = int(nota)
    if nota1 <=10 and nota1 >0:
        print(nota1)
        parada =True
    else:
        print("Somente numeros de 0 a 10")
        nota = input("Digite uma nota de 0 a 10: ")