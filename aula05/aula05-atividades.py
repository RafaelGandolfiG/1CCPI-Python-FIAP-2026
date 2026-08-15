# ATV1
nomes = ["Ana", "Bruno", "Carlos", "Diana"]
for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        print(nomes[i], "e", nomes[j])

# ATV2
matriz = []
numero = 0
for i in range(4):
    matriz.append([])
for i in range(4):
    for j in range(5):
        numero += 1
        matriz[i].append(numero)
for i in range(4):
    for j in range(5):
        print(matriz[i][j], end=' ')
    print()

# contador = 0
# lista = []
# lista1 = []
# for i in range(5 * 4):
#     contador += 1
#     lista.append(contador)
# for i in range(4):
#     lista1.append([])
# contador = 0
# for i in range(4):
#     for j in range(5):
#         lista1[i].append(lista[contador])
#         contador += 1
# for i in range(4):
#     for j in range(5):
#         print(lista1[i][j], end=' ')
#     print()