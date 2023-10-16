# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError("Você está tentando dividir por zero.")
    return True

def deve_ser_int_ou_float(n, d):
    if not isinstance(n, (float, int)):
        raise TypeError(f"{n} deve ser int ou float")
    
    if not isinstance(d, (float, int)):
        raise TypeError(f"{d} deve ser int ou float")


def divide(n, d):
    nao_aceito_zero(d)
    deve_ser_int_ou_float(n, d)
    return n / d

print(divide(8, "0"))