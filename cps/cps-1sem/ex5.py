def pode_aprovar(idade,renda,emprestimo):
    if idade>18 and emprestimo<=20*renda:
        return 'Aprovado'
    else:
        return 'Reprovado'

def definir_taxa(parcelas):
    if parcelas>24 or parcelas<3:
        print('Numero de parcelas invalido')
        exit()
    global taxa
    if parcelas<=6:
        taxa=0.05
        return taxa
    elif parcelas<=12:
        taxa=0.08
        return taxa
    elif parcelas>=13 and parcelas<=24:
        taxa=0.1
        return taxa

def calcular_parcela(emprestimo,taxa,parcelas):
    global pmt
    i=taxa
    n=parcelas
    pmt=emprestimo*(i*(1+i)**n)/(((1+i)**n)-1)
    return pmt

def calcular_total(parcela,parcelas):
    global total
    total=pmt*parcelas
    return total

def calcular_juros(total,emprestimo):
    juros=total-emprestimo
    return juros

nome=input('Digite seu nome: ')
idade=int(input('Digite sua idade: '))
renda=float(input('Digite sua renda: '))
emprestimo=float(input('Digite o valor do empréstimo: '))
parcelas=int(input('Digite o numero de parcelas: '))

    
aprovado=pode_aprovar(idade,renda,emprestimo)

if aprovado=='Aprovado':

    taxa=definir_taxa(parcelas)
    parcela=calcular_parcela(emprestimo,taxa,parcelas)
    total=calcular_total(pmt,parcelas)
    juros=calcular_juros(total,emprestimo)

    print(f'Nome do cliente: {nome}')
    print(f'Valor financiado: {emprestimo}')
    print(f'Taxa de juros: {taxa*100}')
    print(f'Valor da parcela: {round(parcela,2)}')
    print(f'Total pago {round(total,2)}')
    print(f'Total de juros: {round(juros,2)}')
else:
    print('reprovado')