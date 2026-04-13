def calcular_horas_extras(salario_base,horas):
    valor=salario_base*0.015
    total=valor*horas_extras
    return total

def calcular_descontos_faltas(salario_base,faltas):
    desconto=salario_base*0.02*faltas
    return desconto

def calcular_bonus(cargo,recebeu_bonus):
    if recebeu_bonus=='s':
        match cargo:
            case 1:
                return 1000
            case 2:
                return 500
            case 3:
                return 300
            case 4:
                return 100
    return 0

nome=input('Digite o nome do funcionario: ')
cargo=input('1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário\nEscolha: ')
salario_base=float(input('Digite o salario base: '))
horas_extras=float(input('Digite o total de horas extras: '))
faltas=int(input('Total de faltas no mes: '))
bonus=input('Recebeu bonus? ')

extra=calcular_horas_extras(salario_base,horas_extras)
desconto=calcular_descontos_faltas(salario_base,faltas)
bonus=calcular_bonus(cargo,bonus)

acrescimos=extra+bonus
salario_bruto=salario_base+acrescimos
salario_final=salario_bruto-desconto

print(f'Nome do funcionario: {nome}')
print(f'Salario base: {salario_base}')
print(f'Acrescimos: {acrescimos}')
print(f'Descontos: {desconto}')
print(f'Salario bruto: {salario_bruto}')
print(f'salario final: {salario_final}')