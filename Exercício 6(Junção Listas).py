lista1 = []
lista2 = []

for i in range(5):
    num1 = float(input('Digite um número para a primeira lista: '))
    lista1.append(num1)

for i in range(5):
    num2 = float(input('Digite um número para a segunda lista: '))
    lista2.append(num2)

listaFinal = lista1 + lista2

print(f'Primeira lista: {lista1}')
print(f'Segunda lista: {lista2}')
print(f'Lista final: {listaFinal}')