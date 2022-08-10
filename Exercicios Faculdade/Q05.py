##Um determinado clube de futebol pretende classificar seus atletas em categorias. Para isso, o clube contratou você para criar um programa que executasse essa tarefa. Baseada na tabela de categorias do clube, construa um programa que solicite a idade de um atleta e imprima sua categoria;

###De 11 a 15 anos – Juvenil;
##De 16 a 20 anos – Júnior;
##De 21 a 25 anos – Profissional;
idade = int(input("Digite sua idade: "))
if idade <= 5:

  print("Infantil") 

elif idade <= 15:

  print("Juvenil")

elif idade <= 20:

  print("Júnior")

elif idade <= 25:

  print("Profissional")