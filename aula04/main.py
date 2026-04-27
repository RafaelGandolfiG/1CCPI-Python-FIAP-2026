cp=0
while cp<3:
    print('produto')
    cp+=1

cp=0
while cp<10:
    cp+=1
    if cp==3:
        continue
    print(f'produto {cp}')

cp=0
while cp<10:
    cp+=1
    if cp==7:
        break
    print(f'produto {cp}')

n=int(input('Digite um numero n: '))
cont=1
while cont<=n:
    print(cont)
    cont+=1

for cp in range(3):
    print('produto')

