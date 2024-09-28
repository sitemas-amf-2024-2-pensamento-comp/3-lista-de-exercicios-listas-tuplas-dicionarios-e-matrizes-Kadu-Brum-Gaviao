numeros = []

for i in range(10):
    num = float(input('Digite um número: '))
    numeros.append(num)

print(f'O menor número é: {min(numeros)}')
print(f'O maior número é: {max(numeros)}')
