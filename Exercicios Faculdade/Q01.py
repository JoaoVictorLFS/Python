##Faça um programa que receba três notas de um aluno, calcule sua média final e diga se o mesmo está aprovado ou reprovado (se sua média for maior que 5, estará aprovado);
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = (nota1+nota2+nota3)/3

if media >= 5:

  print("Aprovado sua media é {}".format(media))

else:

  print("Reprovado sua media é {}".format(media))

