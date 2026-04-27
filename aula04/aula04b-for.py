for count_music in range(3):
    print(f'Musica {count_music}')

# de 1 até 11, pulando de 2 em 2
for i in range(1, 12, 2):
    print(f'Numero {i}')

for i in range(0,4):
    for j in range(0,3,2):
        print(f'i->{i}, j->{j}')

lista1=['link','baby','jb']
lista2=['link','evidencias','cx']
lista3=['link','boate azul','bm']
lista=[]
lista.append(lista1)
lista.append(lista2)
lista.append(lista3)
for i in range(3):
    for j in range(3):
        print(lista[i][j])