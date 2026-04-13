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

if 10<=codigo<=20:
    precokg=100
elif 21<=codigo<=30:
    precokg=250
elif 31<=codigo<=40:
    precokg=340
else:
    print('codigo da carga invalido')
    exit()


preco=pesokg*precokg
preco_imposto=preco*imposto/100
preco_total=preco+preco_imposto

print(f'Peso em kg {pesokg:.1f}')
print(f'Preço da carga R${preco:.2f}')
print(f'Imposto {imposto}%')
print(f'Preço total R${preco_total:.2f}')