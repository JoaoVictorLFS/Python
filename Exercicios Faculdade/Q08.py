##Cada espectador de um cinema respondeu a um questionário no qual constava sua opinião em relação ao filme: ótimo – 3, bom – 2, regular – 1. Faça um programa que receba a opinião de 15 espectadores, calcule e mostre:

##A quantidade de pessoas que responderam ótimo;
##A quantidade de pessoas que responderam bom;
##A quantidade de pessoas que responderam regular;

otimo = 0

bom = 0
regular = 0

for i in range(0,15):
 codigo = float(input("Digite 1 para REGULAR 2 para BOM 3 para ÓTIMO "))
 if codigo == 1:
  regular += 1
 elif codigo == 2:
   bom += 1
 elif codigo == 3:
  otimo += 1
 else:
  print("valor invalido!")

print("{} REGULAR\n{} BOM\n{} ÓTIMO ".format(regular, bom, otimo))