matriz=[]
for i in range(3):
    matriz.append([])
for i in range(len(matriz)):
    for j in range(3):
        matriz[i].append([])
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end='')
    print()
while True:
    simbolo=input('quem vai jogar? ')
    if simbolo!='x' and simbolo!='o':
        print('simbolo invalido')
        continue
    linha=int(input('linha: '))
    coluna=int(input('coluna: '))
    if matriz[linha][coluna]!=[]:
        print('ja tem nessa posição')
        continue
    matriz[linha][coluna].append(simbolo)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end='')
        print()