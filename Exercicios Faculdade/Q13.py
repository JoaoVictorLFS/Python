##Faça um programa que receba o preço de cinco produtos em uma lista, calcula e exiba:

##A quantidade de produtos com preço inferior a R$ 50,00;
##A quantidade de produtos com preço entre R$ 50,00 e 80,00;
##A quantidade de produtos com preço acima de R$ 80,00
##A média de preço dos produtos;

inferiorA50 = []
entre50E80 = []
maiorQue80 = []
totalDeProdutos = []
media = 0

for i in range(0, 5):
  print("-=" * 30)
  preço = float(input("Digite o preço do produto: "))
  if preço <= 50:
    inferiorA50.append(preço)
  elif preço >= 50 and preço <= 80:
    entre50E80.append(preço)
  elif preço > 80:
    maiorQue80.append(preço)

  totalDeProdutos = inferiorA50 + entre50E80 + maiorQue80
  media = media + totalDeProdutos[i]

media = media / len(totalDeProdutos)

print(media)

menorQue50 = len(inferiorA50)
entre5080 = len(entre50E80)
maiorQ80 = len(maiorQue80)

print("{} produtos inferiores a 50 reais \n{} produtos entre 50 e 80 reais \n{} produtos maiores que 80 reais\nmedia dos preços {}".format(menorQue50, entre5080, maiorQ80, media))