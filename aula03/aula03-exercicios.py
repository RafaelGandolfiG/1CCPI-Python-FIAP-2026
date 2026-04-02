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
nota1=int(input('Digite a nota 1: '))
nota2=int(input('Digite a nota 2: '))
nota3=int(input('Digite a nota 3: '))
nota4=int(input('Digite a nota 4: '))
soma=nota1+nota2+nota3+nota4
media=soma/4
if media>=7:
    print('Aprovado')
elif media>=5 and media<7:
    print('recuperação')
else:
    print('reprovado')

# soma=0
# for i in range(1,5):
#     nota=int(input(f'Digite a nota {i}: '))
#     soma+=nota
#     media=soma/i
# if media>=7:
#     print('Aprovado')
# elif media>=5 and media<7:
#     print('recuperação')
# else:
#     print('reprovado')

# EX5
a=int(input('Digite um numero: '))
b=int(input('Digite outro numero: '))
if a==0 or b==0:
    print('multiplo') 
elif a%b==0 or b%a==0:
    print('multiplo')
else:
    print('nao multiplo')

# EX6
a=float(input('Digite o primeiro numero: '))
b=float(input('Digite o segundo numero: '))
op=input('Digite a operação: ')
match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case _:
        print('nenhuma operação achada')

# conta=input('Digite a conta: ')
# resultado=eval(conta)
# print(resultado)

# EX7
from datetime import datetime
ano_atual = datetime.now().year
nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - nascimento
if idade < 16:
    print("VOTO PROIBIDO")
elif 18 <= idade <= 70:
    print("VOTO OBRIGATORIO")
else:
    print("VOTO OPCIONAL")

# EX8
salario=float(input('Digite o salario: '))
if salario<=280:
    percentual=20
    aumento=0.2*salario
elif salario<=700:
    percentual=15
    aumento=0.15*salario
elif salario<=1500:
    percentual=10
    aumento=0.1*salario
else:
    percentual=5
    aumento=0.05*salario
salario_final=salario+aumento
print(f'Salario de antes: {salario}')
print(f'Porcentagem de aumento: {percentual}%')
print(f'Valor do aumento: R${aumento}')
print(f'Salario final: R${salario_final}')

# EX9
origem=int(input('Digite o codigo de origem: '))
peso=float(input('Digite o peso da carga em toneladas: '))
codigo=int(input('Digite o codigo da carga: '))

match origem:
    case 1:
        imposto=35
    case 2:
        imposto=25
    case 3:
        imposto=15
    case 4:
        imposto=5
    case 5:
        imposto=0
    case _:
        print('codigo invalido')
        exit()

pesokg=peso*1000

if codigo>=10 and codigo<=20:
    precokg=100
elif codigo<=30:
    precokg=250
else:
    precokg=340

preco=pesokg*precokg
preco_imposto=preco*imposto/100
preco_total=preco+preco_imposto

print(f'Peso em kg {pesokg}')
print(f'Preço da carga R${preco}')
print(f'Imposto {imposto}%')
print(f'Preço total R${preco_total}')

# while True: 
#     calcular=input('Quer calcular? ').lower()
    
#     match calcular:
#         case 's':
#             print('vamos calcular...')
#         case 'n':
#             print('saindo...')
#             break
#         case _:
#             print('opção invalida')
#             continue

#     origem=int(input('Digite o codigo de origem: '))
    
#     match origem:
#         case 1:
#             imposto=35
#         case 2:
#             imposto=25
#         case 3:
#             imposto=15
#         case 4:
#             imposto=5
#         case 5:
#             imposto=0
#         case _:
#             print('codigo invalido')
#             continue
    
#     peso=float(input('Digite o peso da carga em toneladas: '))
#     codigo=int(input('Digite o codigo da carga: '))


#     pesokg=peso*1000
    
#     if codigo>=10 and codigo<=20:
#         precokg=100
#     elif codigo<=30:
#         precokg=250
#     else:
#         precokg=340
    
#     preco=pesokg*precokg
#     preco_imposto=preco*imposto/100
#     preco_total=preco+preco_imposto

#     print(f'Peso em kg {pesokg}')
#     print(f'Preço da carga R${preco}')
#     print(f'Imposto {imposto}%')
#     print(f'Preço total R${preco_total}')

# def calcular(origem,peso,codigo):
    
#     match origem:
#         case 1:
#             imposto=35
#         case 2:
#             imposto=25
#         case 3:
#             imposto=15
#         case 4:
#             imposto=5
#         case 5:
#             imposto=0
#         case _:
#             print('codigo invalido')
#             return
        
#     pesokg=peso*1000

#     if codigo>=10 and codigo<=20:
#         precokg=100
#     elif codigo>=21 and codigo<=30:
#         precokg=250
#     else:
#         precokg=340

#     preco=pesokg*precokg
#     preco_imposto=preco*imposto/100
#     preco_total=preco+preco_imposto

#     print(f'Peso em kg {pesokg}')
#     print(f'Preço da carga R${preco}')
#     print(f'Imposto {imposto}%')
#     print(f'Preço total R${preco_total}')
    
# calcular(111,1000,11)

#EX10
a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))
triangulo=False
lados = sorted([a, b, c], reverse=True)
a,b,c=lados
if a>=b+c:
    triangulo=False
else:
    triangulo=True
if triangulo:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    if a==b==c:
        print('equilatero')
    elif a==b or a==c or b==c:
        print('isoceles')
else:
    print('nao triangulo')