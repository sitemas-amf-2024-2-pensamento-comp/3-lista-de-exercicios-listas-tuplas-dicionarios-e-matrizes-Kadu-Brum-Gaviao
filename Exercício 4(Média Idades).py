idade = 1
somaIdades = 0
contadorPessoas = 0

while idade != 0:
    idade = int(input('Cadastre uma idade ou digite 0 para fazer a média: '))
    if idade > 0:
        contadorPessoas += 1
        somaIdades += idade

if contadorPessoas > 0:
    mediaIdade = somaIdades / contadorPessoas
    print(f'A média de idades é: {mediaIdade:.2f}')
else:
    print('Nenhuma idade foi registrada.')
