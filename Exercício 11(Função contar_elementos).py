def contar_elementos(lista_elementos, elemento):
    return lista_elementos.count(elemento)


lista_elementos = [1, 2, 3, 4, 5, 5, 5, 5]
elemento = 5

print(f'O elemento {elemento} aparece {contar_elementos(lista_elementos, elemento)} vezes')
