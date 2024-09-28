def numeros_pares(lista_numeros):
    lista_pares = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)

    return lista_pares


lista_numeros = []

while True:
    num = int(input('Digite um número positivo para ser adicionado à lista, ou um negativo para gerar a lista final:'))
    if num < 0:
        break
    lista_numeros.append(num)

if len(numeros_pares(lista_numeros)) > 0:
    print(f'Números pares: {numeros_pares(lista_numeros)}')
else:
    print('Nenhum número foi inserido...')
