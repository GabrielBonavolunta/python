"""
Calculadora com while
"""

while True:
    numero_um = input("Digite um número: ")
    numero_dois = input("Digite outro número: ")
    operador = input("Digite o operador (+-*/)")

    try:
        numero_um = float(numero_um)
        numero_dois = float(numero_dois)        
    except Exception as error:
        print("Por favor, digite um valor válido.")

    if len(operador) > 1:
        print("Digite apenas 1 operador.")
        continue

    if operador == "+":
            res = numero_um + numero_dois
            print(res)
    elif operador == "-":
            res = numero_um - numero_dois
            print(res)
    elif operador == "*":
            res = numero_um * numero_dois
            print(res)
    elif operador == "/":
            res = numero_um / numero_dois
            print(res)

    sair = input("Quer sair? [s]im: ").lower().startswith("s")
    
    if sair == True:
        break