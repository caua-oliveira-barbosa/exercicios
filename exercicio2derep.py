#Definir o nome e senha
name = input("Digite seu nome de usuario: ")
senha = input("Digite sua senha: ")
parada=False

#Linha de repetição
while parada ==False:
    if name ==senha:
        senha = input("Digite uma senha diferente do nome de usuario: ")
    else:
        print("Seu perfil foi criado com sucesso.")
        parada =True