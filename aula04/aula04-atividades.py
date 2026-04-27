# ATV2
# def validar_nota(nota):
#     while nota>10 or nota<0:
#         print('nota invalida')
#         nota=float(input('Digite a nota: '))
#     return nota
# nota1=float(input('Digite a nota 1: '))
# nota1=validar_nota(nota1)
# nota2=float(input('Digite a nota 2: '))
# nota2=validar_nota(nota2)
# soma=nota1+nota2
# media=soma/2
# print(media)

soma=0
for i in range(1,3):
    nota=float(input('Digite a nota: '))
    while nota>10 or nota<0:
        print('nota invalida')
        nota=float(input('Digite a nota: '))
    soma+=nota
    media=soma/i
print(media)

# ATV3
n=int(input('Digite a quantidade: '))
for i in range(n):
    print(f'produto {i}')