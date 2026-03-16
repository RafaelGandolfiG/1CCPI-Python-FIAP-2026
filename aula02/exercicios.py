#EX1
pi=3.14159
raio=5
#raio=float(input('Raio do circulo: '))
print(pi*(raio**2))

#EX2
fahrenheit=float(input('Temperatura em Farenheit: '))
celsius=(fahrenheit-32)*5/9
print(celsius)

#EX3
fahrenheit=float(input('Temperatura em Farenheit: '))
celsius=(fahrenheit-32)*5/9
print(celsius)

#EX4
livros=3
#livros=int(input("quantos livros: "))
canetas=2
#canetas=int(input('quantas canetas: '))
preco_livro=25.0
preco_caneta=5.0
total=(livros*preco_livro)+(canetas*preco_caneta)
print(f'O total é {total}')

#EX5
velocidade=60.0
#velocidade=float(input('digite a velocidade: '))
distancia=150.0
#distancia=float(input('Digite a distancia: '))
tempo=distancia/velocidade
print(f'o tempo foi de {tempo}')

#EX6
nota1=float(input('Digite a nota 1: '))
nota2=float(input('Digite a nota 2: '))
media=(nota1+nota2)/2
print(media)
'''
    contador=0
    soma=0
    while contador<2:
        nota=float(input(f'Digite a nota {contador+1}: '))
        soma+=nota
        contador+=1
        media=soma/contador
    print(media)
'''

#EX7
nota1=float(input('Digite a nota 1: '))
nota2=float(input('Digite a nota 2: '))
peso1=nota1*4
peso2=nota2*6
media=(peso1+peso2)/10

#EX8
nome1=input('Digite o nome da peça 1: ')
numero1=int(input('Digite a quantidade de peças 1: '))
valor1=float(input('Digite o valor de cada peça 1: '))
nome2=input('Digite o nome da peça 2: ')
numero2=int(input('Digite a quantidade de peças 2: '))
valor2=float(input('Digite o valor de cada peça 2: '))
total=(numero1*valor1)+(numero2*valor2)
print(total)
'''
    total1=0
    for i in range(3):
        nome=input(f'Digite o nome da peça {i+1}: ')
        quantidade=int(input(f'Digite a quantidade da peça {i+1}: '))
        preco=float(input(f'Digite o preço da peça {i+1}: '))
        total=quantidade*preco
        total1+=total
        print(nome)
        print(total)
    print(total1)
'''

#EX9
valor=float(input('Digite o valor da compra: '))
pago=float(input('Digite o valor pago: '))
troco=pago-valor
print(troco)
'''
    i=0
    total=0
    while True:
        preco=float(input(f'Digite o preco {i+1}: '))
        if preco<0:
            break
        i+=1
        total+=preco
    print(f'------Total: {total}------')
    print(f'------Quantidade: {i}------')
    pago=float(input('Digite o valor pago: '))
    troco=pago-total
    print(f'O troco é de {troco}')
'''