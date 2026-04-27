# EX1
import random
lista=[]
n=int(input('Digite a quantidade de valores: '))
for i in range(n):
    numero=random.randint(1,10)
    lista.append(numero)
print(lista)

# EX2
soma=0
notas=[]
n=int(input('Digite a quantidade de alunos: '))
for i in range(1,n+1):
    nota=float(input('Digite a nota: '))
    notas.append(nota)
    soma+=nota
    media=soma/i
print(media)
iguais=0
acima=0
abaixo=0
for nota in notas:
    if nota==media:
        iguais+=1
    elif nota<media:
        abaixo+=1
    else:
        acima+=1
print(iguais)
print(acima)
print(abaixo)

# EX3
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(12):
    print(f"O mês de {meses[i]} tem {dias[i]} dias ao todo.")

# EX4
soma=0
numeros=[]
tamanho=int(input('Digite o tamanho da lista: '))
for i in range(tamanho):
    numero=int(input('Digite o numero: '))
    numeros.append(numero)
for numero in numeros:
    soma+=numero
print(soma)

# EX5
lista=[]
while True:
    palavra=input('Digite uma palavra: ')
    if palavra=='':
        break
    lista.append(palavra)
reverso=sorted(lista, reverse=True)
print(reverso)

# EX6
n = int(input("Digite n (>0): "))
vetor = []
for i in range(n):
    c = input(f"Caractere {i+1}: ")
    vetor.append(c)
i = 0
j = n - 1
while i < j:
    temp = vetor[i]
    vetor[i] = vetor[j]
    vetor[j] = temp
    i += 1
    j -= 1
print("Vetor invertido:", vetor)

# EX7
import random
matriz=[]
for i in range(3):
    matriz.append([])
for i in range(3):
    for j in range(4):
        aleatorio=random.randint(1,10)
        matriz[i].append(aleatorio)
        print(matriz[i][j],end=' ')
    print()

# EX8
matriz1=[]
matriz2=[]
matriz3=[]
linhas=int(input('Digite o numero de linhas: '))
colunas=int(input('Digite o numero de colunas: '))
for i in range(linhas):
    matriz1.append([])
    matriz2.append([])
    matriz3.append([])
print('----------Matriz1----------')
for i in range(linhas):
    for j in range(colunas):
        numero=int(input('Digite um numero: '))
        matriz1[i].append(numero)
print('----------Matriz2----------')
for i in range(linhas):
    for j in range(colunas):
        numero=int(input('Digite um numero: '))
        matriz2[i].append(numero)
print('----------Matriz SOMA----------')
for i in range(linhas):
    for j in range(colunas):
        matriz3[i].append(matriz1[i][j]+matriz2[i][j])
print('----------Matriz----------')
for i in range(linhas):
    for j in range(colunas):
        print(matriz3[i][j],end=' ')
    print()