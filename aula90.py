import sys

# Generation expression, Iterables e Iterators em Python
iterable = ["Eu", "Tenho", "__iter__"]
iterator = iter(iterable)
lista = [n for n in range(10000)]
generator = (n for n in range(10000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

for n in generator:
    print(n)