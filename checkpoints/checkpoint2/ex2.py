a=int(input('Digite o lado a: '))
b=int(input('Digite o lado b: '))
c=int(input('Digite o lado c: '))

triangulo=False

if a>b and a>c:
    maior=a
elif b>a and b>c:
    maior=b
else:
    maior=c
    
if maior==a:
    A=a
    if b>c:
        B=b
        C=c
    else:
        B=c
        C=b
elif maior==b:
    A=b
    if a>c:
        B=a
        C=c
    else:
        B=c
        C=a
else:
    A=c
    if a>b:
        B=a
        C = b
    else:
        B=b
        C=a
        
print(A,B,C)

if A>=B+C:
    triangulo=False
else:
    triangulo=True
if triangulo:
    if A**2==B**2+C**2:
        print('triangulo retangulo')
    elif A**2>B**2+C**2:
        print('triangulo obtusangulo')
    elif A**2<B**2+C**2:
        print('triangulo acutangulo')
    if A==B==C:
        print('equilatero')
    elif A==B or A==C or B==C:
        print('isoceles')
else:
    print('nao triangulo')