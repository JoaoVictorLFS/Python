#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Salário: maior que zero;
#Estado Civil: 's', 'c', 'v', 'd'

nome = str(input("Digite seu nome "))
while len(nome) <= 3: 
        print("nome invalidado, digite novamente!")
        print("o nome deve ter no minimo 4 caracteres")
        nome = str(input("Digite seu nome "))

idade = int(input("Digite sua idade: "))   
while idade > 150 or idade < 0:
    print("idade invalida, Digite novamente: ")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salario"))   
while salario < 0:
    print("salario invalido, digite novamente!")
    salario = float(input("Digite seu salario"))

sexo = str(input("digite seu sexo: "))
while sexo != "f" and sexo != "m":
    print("sexo invalido, digite novamente")
    sexo = str(input("digite seu sexo: "))
    
estadoCivil = str(input("digite seu estado civil: "))  
while estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d":
    print("estado civil invalido, digite novamente")
    estadoCivil = str(input("digite seu estado civil: "))  














