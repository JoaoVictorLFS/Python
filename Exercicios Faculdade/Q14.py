##Faça um programa para uma padaria utilizando lista:
##Receba um produto por vez e a quantidade dele
##O usuário deve informar quando não quiser comprar mais nada
##Calcule o valor total e apresente a lista de produtos e quantidades compradas
##Se ele tiver comprado mais de 5 unidades de um produto, deve receber um desconto de 10% nele (e ser avisado sobre isso)

##PRODUTOS:
##Pão baguete - R$1,25 Torrada - R$ 4,30
##Pão doce - R$0,50 Café - R$1,30
##Tapioca - R$3,50 Sonho - R$ 2,35
import os

produtos = ["Pão-baguete", "pão doce", "tapioca", "torrada", "café", "sonho"]
precos = [1.25, 0.50, 3.50 , 4.30, 1.30, 2.35]
produtosConsumidos = []
quantidadeDeProdutosConsumidos = []
quantidade = 0
valorBruto = 0

while True:

  os.system('cls')

  print("-=-" * 30)

  print("[1] Pão-Baguete [R$ 1,25]\n[2] Pão Doce  [R$ 0,50]\n[3] Tapioca  [R$ 3,50]\n[4] Torrada  [R$ 4,30]\n[5] Café    [R$ 1,30]\n[6] Sonho   [R$ 2,35]")

  print("-=-" * 30)

  

  codigo = int(input("Digite uma opção: "))

  

  while codigo not in [1, 2, 3, 4, 5, 6]:
    
    os.system('cls')
    print("-=-" * 30)
    print("[1] Pão-Baguete [R$ 1,25]\n[2] Pão Doce  [R$ 0,50]\n[3] Tapioca  [R$ 3,50]\n[4] Torrada  [R$ 4,30]\n[5] Café    [R$ 1,30]\n[6] Sonho   [R$ 2,35]")

    print("-=-" * 30)
    print("Erro!\nDigite Novamente!")
    codigo = int(input("Digite uma opção: "))
  quantidades = int(input("Digite a quantidade: "))

  if codigo == 1:
    produtosConsumidos.append("Pão-Baguete")
    produtosConsumidos.append(quantidades)
    quantidade += quantidades
    valorBruto += precos[0] * quantidades

  elif codigo == 2: 
    produtosConsumidos.append("Pão Doce")
    produtosConsumidos.append(quantidades)
    quantidade += quantidades
    valorBruto += precos[1] * quantidades

  elif codigo == 3: 
    produtosConsumidos.append("tapioca")
    produtosConsumidos.append(quantidades)
    quantidade += quantidades
    valorBruto += precos[2] * quantidades

  elif codigo == 4: 
    produtosConsumidos.append("Torrada")
    produtosConsumidos.append(quantidades)
    quantidade += quantidades
    valorBruto += precos[3] * quantidades

  elif codigo == 5: 
    produtosConsumidos.append("café")
    produtosConsumidos.append(quantidades)
    quantidade += quantidades
    valorBruto += precos[4] * quantidades
  
  elif codigo == 6: 
    produtosConsumidos.append("Sonho")
    produtosConsumidos.append(quantidades)
    quantidade += quantidades
    valorBruto += precos[5] * quantidades
  
  else:
    print("Digite uma opção viavel")
  os.system('cls')
  dejacontinuar = int(input("Deseja continuar?\n[1] Sim\n[2] Não "))
  if dejacontinuar == 1:
    os.system('cls')
    pass
  
  elif dejacontinuar == 2:
    os.system('cls')
    if quantidade > 5:
      desconto = valorBruto * 0.10
      valorComdesconto = valorBruto - desconto
      print("-=-" * 30)
      print("itens comprados: ")
      print("\n".join(map(str, produtosConsumidos)))
      print("-=-" * 30)
      print("Foi comprado um total de {} itens".format(quantidade))
      print("Valor Bruto da compra é de {}, desconto de {}".format(valorBruto, desconto))
      print("Valor Total é de {}".format(valorComdesconto))
      break

    else:
      print("-=-" * 30)
      print("itens comprados: ")
      print("\n".join(map(str, produtosConsumidos)))
      print("-=-" * 30)
      print("Foi comprado um total de {} itens".format(quantidade))
      print("Valor total da compra é de {}".format(valorBruto))
      break

  else:
    print("digite uma opção viavavel")