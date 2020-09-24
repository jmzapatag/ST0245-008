def p1(elementos):
    lista2 = []
    for i in elementos:
        if i not in lista2:
            lista2.append(i)
    return lista2
lista = [4,7,11,4,9,5,11,7,3,5]
final = p1(lista)
print(final)
