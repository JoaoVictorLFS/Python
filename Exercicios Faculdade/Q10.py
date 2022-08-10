##Faça um programa que lê o sexo de 3 pessoas em uma lista, calcula e exibe a quantidade de pessoas de cada sexo
sexosMasculino = []
sexosFemininos = []

for i in range(0, 3):
  sexo = str(input("digite o seu sexo: "))
  if sexo == "masculino":
    sexosMasculino.append(sexo)
  elif sexo == "feminino":
    sexosFemininos.append(sexo)
  else:
    print("erro")

print("A",len(sexosMasculino), "pessoas do sexo masculino", "e a", len(sexosFemininos), "do sexo feminino")