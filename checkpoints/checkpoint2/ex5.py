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
        return '5% ao mes'
    elif parcelas<=12:
        taxa=0.08
        return '8 % ao mes'
    elif parcelas>=13 and parcelas<=24:
        taxa=0.1
        return '10% ao mes'

def calcular_parcela(emprestimo,taxa,parcelas):
    i=taxa
    n=parcelas
    pmt=valor*(i*(1+i)**n)/(((1+i)**n)-1)
    return pmt

nome=input('Digite seu nome: ')
idade=int(input('Digite sua idade: '))
renda=float(input('Digite sua renda: '))
emprestimo=float(input('Digite o valor do empréstimo: '))
parcelas=int(input('Digite o numero de parcelas: '))

    
aprovado=pode_aprovar(idade,renda,valor)
taxa=definir_taxa(parcelas)
parcela=calcular_parcela(emprestimo,taxa,parcelas)
total=calcular_total(parcela,parcelas)
juros=calcular_juros(total,valor)