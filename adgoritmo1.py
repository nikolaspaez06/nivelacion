#Este algoritmo ordena una lista de números ingresados por el usuario 
# utilizando el método de ordenamiento por selección.


lista = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
for i in range(len(lista)):
    minimo = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[minimo]:
            minimo = j
    lista[i], lista[minimo] = lista[minimo], lista[i]
print("La lista ordenada es:", lista)
