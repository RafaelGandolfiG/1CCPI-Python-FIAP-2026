# EX1
from playsound import playsound
numero=input('Digite um numero: ')
try:
    numero=int(numero)
except Exception as erro:
    print(erro)
    playsound(r"C:\Users\Rafael\Documents\1CCPI-Python-FIAP-2026\aula03\faaah.mp3")

#EX2
numero=int(input('Digite um numero: '))
if numero%2==0:
    print('par')
else:
    print('impar')

# EX3
numero1=int(input('Digite um numero: '))
numero2=int(input('Digite outro numero: '))
if numero1>numero2:
    print('o primeiro é maior')
elif numero2>numero1:
    print('O segundo é maior')
else:
    print('Sao iguais')

# numeros=[]
# for i in range(2):
#     numero=int(input('Digite um numero: '))
#     numeros.append(numero)
# if numeros[0]==numeros[1]:
#     print('iguais')
#     exit()
# print(f'Maior numero {max(numeros)}')

# EX4
