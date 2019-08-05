# dada uma lista
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# imprima o maior elemento
print('Maior elemento: ',max(lista))

# imprima o menor elemento
print('Menor elemento: ', min(lista))

# imprima os numeros pares
print('Numeros pares:')
for a in range(0, len(lista)):
    if lista[a] % 2 == 0 and lista[a] > 0:
        print(lista[a])

# imprima o numero de ocorrências do primeiro elemento
print('Numero de ocrrencias do {}: {}'.format(lista[0], lista.count(lista[0])))

# imprima a media dos elementos
soma = 0
for b in range(0, len(lista)):
    soma += lista[b]
media = soma/len(lista)
print('Media dos elementos: {:.2f}'.format(media))

# imprima a soma dos elementos negativos
soma_dos_elementos_negativos = 0
for c in range(0, len(lista)):
    if lista[c] < 0:
        soma_dos_elementos_negativos += lista[c]
print('Soma dos elementos negativos: ', soma_dos_elementos_negativos)
