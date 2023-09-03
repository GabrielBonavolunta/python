# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

funcao_mult = mult(1,2,3,4,5)
print(funcao_mult)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    elif numero % 2 == 1:
        return "Ímpar"
    

funcao_par_ou_impar = par_ou_impar(2)
print(funcao_par_ou_impar)