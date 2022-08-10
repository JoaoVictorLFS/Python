##Cada espectador de um cinema respondeu a um questionário no qual constava sua opinião em relação ao filme: ótimo – 3, bom – 2, regular – 1. Faça um programa que receba a opinião de 5 espectadores em uma lista, calcule e mostre a quantidade de pessoas que responderam ótimo, bom e regular.
otimos = []
bons = []
regulars = []

for i in range(0, 5):

  print("-=" * 30)

  codigo = int(input("[1] Regular\n[2] Bom\n[3] Otimo\nDigite uma opção: "))
  if codigo == 1:
    otimos.append(codigo)
  elif codigo == 2:
    bons.append(codigo)
  elif codigo == 3:
    regulars.append(codigo)

otimo = len(otimos)
bom = len(bons)
regular = len(regulars)

print("A", otimo, "otimos", "a", bom, "bons", regular, "regular")

  