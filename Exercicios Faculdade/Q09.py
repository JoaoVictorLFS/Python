##Faça um programa que receba 6 números inteiros em uma lista e mostra apenas os números positivos;
numerospositivos = []

for i in range(0, 6):
  numero = int(input("digite um numero: "))
  if numero > 0:
    numerospositivos.append(numero)

print(numerospositivos)


  