eng2sp=dict()
print(eng2sp)

eng2sp['one']='uno'
print(eng2sp)

eng2sp={
    'one':'uno',
    'two':'dos',
    'three':'tres'
}
print(eng2sp['two'])

print(len(eng2sp))

# Operador in
print('one' in eng2sp)
print('uno' in eng2sp)

# valores
valores_dict=eng2sp.values()
print('uno' in valores_dict)

# contador de letras
print()

def count_letters(palavra):
    d=dict()
    for c in palavra:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d

dict_contagem=count_letters('paralelepipedo')
print(dict_contagem)