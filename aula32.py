"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#numero = input("Digite um número inteiro: ")

#if numero.isdigit():
 #   numero = int(numero)
  #  if numero % 2 == 0:
   #     print("O número é par.")
    #elif numero % 2 == 1:
     #   print("O número é ímpar.")
#else:
 #   print("O que você digitou não é um número inteiro.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#hora = input("Digite a hora [0 até 23]: ")

#try:
   # hora = int(hora)

   # if hora >= 0 and hora <= 11:
       # print("Bom dia!")
  #  elif hora >= 12 and hora <= 17:
       # print("Boa tarde!")
   # elif hora >= 18 and hora <= 23:
       # print("Boa noite!")
   # else:
       # print("Não conheço essa hora.")
#except:
   # print("Por favor, digite apenas números inteiros.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome: ")

if len(nome) <= 4:
    print("Seu nome é muito curto.")
elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal.")
elif len(nome) > 6:
    print("Seu nome é muito grande.")