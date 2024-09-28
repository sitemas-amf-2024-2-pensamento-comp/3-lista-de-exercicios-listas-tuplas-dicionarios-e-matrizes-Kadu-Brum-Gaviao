matriz_numeros = [
    [2, 4],
    [6, 8]
]
somaMatriz = 0

for linha in matriz_numeros:
    for elemento in linha:
        somaMatriz += elemento
print(f'A soma de todos os elementos da matriz é: {somaMatriz}')
