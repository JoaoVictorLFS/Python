##Faça um programa que recebe o preço de 10 produtos e exibe o valor do produto mais caro;

maior = 0

for i in range(0,15):

 valorproduto = float(input("Digite o valor do produto: "))

 if valorproduto > maior:

  maior = valorproduto

print("o produto mais caro foi {}".format(maior))