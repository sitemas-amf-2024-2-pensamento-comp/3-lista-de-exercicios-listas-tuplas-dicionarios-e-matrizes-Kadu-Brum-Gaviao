def maior_numero(lista_numeros):
    return max(lista_numeros)


lista_numeros = []

for i in range(5):
    num = int(input('Digite um número para ser colocado na lista: '))
    lista_numeros.append(num)

print(f'O maior número da lista é: {maior_numero(lista_numeros)}')
