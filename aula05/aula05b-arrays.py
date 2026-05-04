lista_frutas=['maçã','banana','pêssego']
print(lista_frutas[0])
print(lista_frutas[1])
print(lista_frutas[2])

lista_frutas.append('uva')

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)