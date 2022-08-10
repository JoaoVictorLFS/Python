#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

nomeDoUsuario = str(input("Digite o usuario: "))
senha = str(input("Digite sua senha: "))
while senha == nomeDoUsuario:
    print("senha igual ao nome do usuário")
    senha = str(input("Digite sua senha: "))
