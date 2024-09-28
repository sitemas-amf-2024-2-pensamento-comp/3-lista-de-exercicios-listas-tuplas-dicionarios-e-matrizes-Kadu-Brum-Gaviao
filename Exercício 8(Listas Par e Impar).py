listaPar = []
listaImpar = []

for i in range(10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

print(f'Os números da lista par são: {listaPar}')
print(f'Os números da lista impar são: {listaImpar}')