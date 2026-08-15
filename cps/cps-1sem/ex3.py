cp1=float(input('Digite a nota da cp1: '))
cp2=float(input('Digite a nota da cp2: '))
cp3=float(input('Digite a nota da cp3: '))
s1=float(input('Digite a nota da sprint1: '))
s2=float(input('Digite a nota da sprint2: '))
gs=float(input('Digite a nota da global solution: '))

if cp1<=10 and cp2<=10 and cp3<=10:
    if cp1<cp2 and cp1<cp3:
        menor=cp1
        soma_cp=cp2+cp3
    elif cp2<cp1 and cp2<cp3:
        menor=cp2
        soma_cp=cp1+cp3
    else:
        menor=cp3
        soma_cp=cp1+cp2
else:
    print('nota da cp invalida')
    exit()

if s1<=10 and s2<=10:
    soma_s=s1+s2
else:
    print('nota da sprint invalida')
    exit()

if gs<=10:
    gs=gs
else:
    print('nota da global solution invalida')
    exit()

media=((cp1+cp2+cp3-menor+s1+s2)/4)*0.4+(gs * 0.6)
media_com_peso=media*0.4

print(f'Media do semestre: {media:.1f}')
print(f'Media com peso: {media_com_peso:.1f}')