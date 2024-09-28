def media(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)
    # sum calcula a soma da lista e len calcula a quantidade de elementos


lista_numeros = []

while True:
    num = int(input('Digite um número para ser colocado na lista(ou digite um número abaixo de zero para parar): '))
    if num < 0:
        break
    lista_numeros.append(num)

if len(lista_numeros) > 0:
    print(f'A média dos números é: {media(lista_numeros)}')
else:
    print('Nenhum número foi inserido...')