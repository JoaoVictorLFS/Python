produtos = ["pão baguete", "pão doce", "tapioca", "torrada", "café", "sonho"]
precos = [1.25, 0.5, 3.5, 4.3, 1.3, 2.35]
quantidades = [0,0,0,0,0,0]
resposta = "sim"

while(resposta == "sim"):
    print("VAMOS INSERIR UM PRODUTO: ")
    produto = input("Produto >>> ")

    while(produto != "pão baguete" and produto != "pão doce" and produto != "tapioca" and
        produto != "torrada" and produto != "café" and produto != "sonho"):
        print("Valor inválido!")
        produto = input("Produto >>> ")

    quantidade = int(input("Quantidade >>> "))

    while(quantidade <= 0):
        print("Valor inválido!")
        quantidade = int(input("Quantidade >>> "))

    indice = produtos.index(produto) #produtos.index("pão baguete)
    quantidades[indice] = quantidade

    resposta = input("Deseja inserir mais algum produto? DIGITE sim OU não! >>> ")
    while(resposta != "sim" and resposta != "não"):
        print("Valor inválido!")
        resposta = input("DIGITE sim OU não! >>> ")

#print(quantidades)
valorTotal = 0

print("--- COMANDA ---")
for x in range(len(quantidades)):
    if(quantidades[x] > 0):
        print(produtos[x], "-", quantidades[x], "unidades")
    if(quantidades[x] > 5):
        precos[x] = 0.9 * precos[x]
        print("     * desconto de 10%")
    valorTotal += quantidades[x] * precos[x]

print("Valor total = R$", valorTotal)
