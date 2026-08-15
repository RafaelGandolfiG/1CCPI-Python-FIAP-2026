# Ex1
pergunta=input('quer exibir a mensagem? ')
while pergunta=='s':
    print('ola mundo')
    pergunta=input('quer exibir novamente? ')

# Ex2
for i in range(0,110,10):
    print(i)

# Ex3
numero=int(input('digite um numero: '))
while numero<0:
    print('digite um numero positivo')
    numero=int(input('digite um numero: '))
soma=0
for i in range(1,numero+1):
    soma+=i
print(soma)

# Ex4
numero=int(input('digite um numero: '))
for i in range(1,numero+1):
    if numero%i==0:
        print(i)

# Ex5
for numero in range(2, 2001):
    primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break
    if primo:
        print(numero)

# Ex6
import random
numero=int(input('digite um numero: '))
while numero<0:
    print('digite um numero positivo')
    numero=int(input('digite um numero: '))
lista=[]
for i in range(numero):
    aleatorio=random.randint(1,20)
    lista.append(aleatorio)
print(lista)

# Ex7
import random
numero = int(input('digite um numero: '))
while numero < 0:
    print('digite um numero positivo')
    numero = int(input('digite um numero: '))
lista = []
for i in range(numero):
    aleatorio = random.randint(1, 20)
    lista.append(aleatorio)
print(f'lista antes de inverter {lista}')
invertida = []
for i in range(len(lista)):
    invertida.append(lista[-1-i])
print(f'lista depois de inverter {invertida}')

# Ex8
linhas=int(input('digite o numero de linhas: '))
colunas=int(input('digite o numero de colunas: '))
matriz1=[]
matriz2=[]
matrizsoma=[]
for i in range(linhas):
    matriz1.append([])
    matriz2.append([])
    matrizsoma.append([])
for i in range(len(matriz1)):
    for j in range(colunas):
        numero=int(input('digite um numero: '))
        matriz1[i].append(numero)
for i in matriz1:
    for j in i:
        print(j, end='')
    print()
for i in range(len(matriz2)):
    for j in range(colunas):
        numero=int(input('digite um numero: '))
        matriz2[i].append(numero)
for i in matriz2:
    for j in i:
        print(j, end='')
    print()
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        matrizsoma[i].append(matriz1[i][j]+matriz2[i][j])
for i in matrizsoma:
    for j in i:
        print(j, end='')
    print()