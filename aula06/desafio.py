def detectar(endpoint):
    lista=[]
    for i in range(len(endpoint)):
        if 200<=endpoint[i]<=299:
            lista.append(True)
        else:
            lista.append(False)
    for i in range(len(lista)-1):
        if not lista[i] and not lista[i+1]:
            return "seguidos"
    else:
        return "nao seguidos"
def classificar(endpoint,msg):
    bom=0
    mal=0
    for i in range(len(endpoint)):
        if endpoint[i]>=200 and endpoint[i]<=299:
            bom+=1
        else:
            mal+=1
    conta=(bom*100)/(bom+mal)
    if msg=='seguidos':
        return 'critico', mal, conta
    elif conta>=80:
        return 'estavel', mal, conta
    elif conta<80:
        return 'instavel', mal, conta
status=[
    [200,200,401,200,500],
    [200,200,200,200,200],
    [201,500,502,201,500]
]
endpoints=['/login','/produtos','/pedidos']
piores=[]
for i in range(len(endpoints)):
    print(f'analisando o endpoint {endpoints[i].replace('/','')}')
    seguido=detectar(status[i])
    clas,mal,pctg=classificar(status[i],seguido)
    print(f'endpoint {clas}')
    print(f'porcentagem de sucessos {pctg}%')
    print('='*20)
    piores.append(mal)
maior=0
for i in range(len(piores)):
    if piores[i]>maior:
        maior=piores[i]
        pior=endpoints[i]
print(f'pior endpoint {pior}')