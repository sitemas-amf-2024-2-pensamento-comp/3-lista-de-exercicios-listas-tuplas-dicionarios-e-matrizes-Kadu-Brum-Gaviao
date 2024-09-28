lista1 = []
lista2 = []

for i in range(5):
    num1 = float(input('Digite um número para a primeira lista: '))
    lista1.append(num1)

for i in range(5):
    num2 = float(input('Digite um número para a segunda lista: '))
    lista2.append(num2)

comuns = list(set(lista1) & set(lista2))

print(f'Os elementos comuns da lista é: {comuns}')