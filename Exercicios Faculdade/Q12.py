##Faça um programa que lê 4 números reais em uma lista, calcula e exibe a quantidade de números negativos e a soma dos números positivos dessa mesma lista;
numerosNegativos = []
numerosPositivos = []
soma = 0

for i in range(0, 5):
    numero = float(input("Digite um numero: "))
    if numero < 0:
        numerosNegativos.append(numero)
    elif numero > 0:
        numerosPositivos.append(numero)
    
soma = sum(numerosPositivos)
negativo = len(numerosNegativos)
positivos = len(numerosPositivos)

print("{} Numeros Negativos\n{} Numeros positivos\n{} A soma de todos os numeros positivos".format(negativo, positivos, soma))