# EX1
while True:
    print('Hello, World')
    continuar=input('Deseja continuar? ').lower()
    if continuar=='s':
        continue
    else:
        print('fim')
        break
    
# EX2
for i in range(0,110,10):
    print(i)

# EX3
numero=int(input('Digite um numero: '))
for i in range(1,26):
    print(f'{numero} * {i} = {i*numero}')

# for i in range(1,11):
#     for j in range(1,26):
#         print(f'{i} * {j} = {i*j}')

# EX4
lista=[]
for i in range(5):
    numero=int(input('Digite um numero: '))
    lista.append(numero)
print(sum(lista))

# EX5
lista=[]
for i in range(5):
    numero=int(input('Digite um numero: '))
    lista.append(numero)
print(max(lista))

# EX6
numero=int(input('Digite um numero: '))
for i in range(2,numero):
    if i%2==0:
        print(i)

# EX7
soma=0
numero=int(input('Digite um numero: '))
for i in range(numero+1):
    soma+=i
print(soma)

# EX8
numero=int(input('Digite um numero: '))
for i in range(numero+1):
    if i>0 and numero%i==0:
        print(i)

# EX9
for num in range(2, 2001):
    eh_primo = True  
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break  
    if eh_primo:
        print(num)