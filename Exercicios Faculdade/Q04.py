##Faça um programa que calcula e exibe o salário reajustado de um funcionário. O percentual de aumento encontra-se na tabela a seguir;
##Até R$300 --> 35%
##Acima de R$300 --> 15%
salario = float(input("digite o seu salario: "))

if (salario <= 300):

  reajuste = salario * 1.35

  print("novo salario é de: {}".format(reajuste))

else:

  reajuste = salario * 1.15

  print("novo salario é de: {}".format(reajuste))