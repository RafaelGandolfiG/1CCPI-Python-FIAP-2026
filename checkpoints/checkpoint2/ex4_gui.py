#DEFINIÇÕES
def calcular_horas_extras(salario_base, horas):
    horas_extras = salario_base * 0.015
    total_extras = horas_extras * horas
    return total_extras

def calcular_descontos_faltas(salario_base, faltas):
    desconto_falta = salario_base * 0.02
    total_desconto = desconto_falta * faltas
    return total_desconto

def calcular_bonus(cargo,recebeu_bonus):
    if recebeu_bonus=='S':
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


#PROGRAMA PRINCIPAL
nome = str(input('Digite o nome do funcionário:'))
cargo = int(input('Digite o valor que corresponde ao cargo do funcionário: 1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário '))
salario_base = float(input('Digite o salário base do funcionário:'))
horas = int(input('Digite quantas horas extras o funcionário teve:'))
faltas = int(input('Digite quantas faltas teve o funcionário:'))
recebeu_bonus = str(input('O funcionário recebeu bônus:[S/N]')).strip().upper()[0]

valor_recebido_extras = calcular_horas_extras(salario_base,horas)
valor_recebido_bonus = calcular_bonus(cargo,recebeu_bonus)
valor_descontos = calcular_descontos_faltas(salario_base, faltas)
total_acrescimos = valor_recebido_bonus + valor_recebido_extras
total_descontos = calcular_descontos_faltas(salario_base, faltas)
salario_final = salario_base + total_acrescimos - total_descontos

#OQUE APARECERÁ NA SAÍDA
print(f'O salário bruto é de {salario_base}')
print(f'O total de acréscimos é de R${total_acrescimos}')
print(f'O total de descontos foi de R${total_descontos}')
print(f'O salário final do funcionário foi de R${salario_final}')