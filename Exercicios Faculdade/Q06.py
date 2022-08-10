##Faça um programa que lê a resposta de 15 usuários para a seguinte pergunta: “Você gosta de beterraba? Digite 1 para SIM e 2 para NÃO”. Após a coleta da resposta de cada usuário, o algoritmo deverá exibir a quantidade de respostas para cada opção;
sim = 0
nao = 0

for i in range(0,15):
 codigo = float(input("Digite 1 para SIM e 2 para NÃO "))
 if codigo == 1:
  sim += 1
 elif codigo == 2:
  nao += 1
 else:

  print("valor invalido!")

print("{} Sim\n{} Não ".format(sim, nao))