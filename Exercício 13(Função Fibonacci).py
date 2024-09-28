def fibonacci(n):
    lista_fibonacci = []
    a, b = 0, 1

    for i in range(n):
        lista_fibonacci.append(a)
        a, b = b, a + b

    return lista_fibonacci


num = int(input('Quantos números você quer ver na lista: '))

print(fibonacci(num))
