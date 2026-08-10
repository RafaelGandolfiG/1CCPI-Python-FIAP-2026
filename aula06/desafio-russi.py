status=[
    [200,200,401,200,500],
    [200,200,200,200,200],
    [201,500,502,201,500]
]
endpoints=['/login','/produtos','/pedidos']
def eh_sucesso(codigo):
    return codigo>=200 and codigo<=299
def erros_seguidos(requisicoes):
    for i in range(len(requisicoes)-1):
        codigo_atual=requisicoes[i]
        prox_codigo=requisicoes[i+1]
        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    else:
        return True
def analisar_endpoint(requisicoes):
    qtd_sucessos=0
    for codigo in requisicoes:
        if eh_sucesso(codigo):
            qtd_sucessos+=1
    qtd_requisicoes=len(requisicoes)
    qtd_erros=qtd_requisicoes-qtd_sucessos
    percentual_sucessos=(qtd_sucessos/qtd_requisicoes)*100
    tem_erros_seguidos=erros_seguidos(requisicoes)
    if tem_erros_seguidos:
        classificacao='critico'
    elif percentual_sucessos>=80:
        classificacao='estavel'
    else:
        classificacao='instavel'
    return (
        qtd_sucessos,
        qtd_erros,
        percentual_sucessos,
        classificacao
    )
maior_qtd_erros=-1
endpoint_maior_erro=''
for i in range(len(endpoints)):
    nome_endpoint=endpoints[i]
    status_endpoint=status[i]
    sucessos,erros,percentual,classificacao=analisar_endpoint(status_endpoint)
    print(f'Endpoint: {nome_endpoint}')
    print(f'Sucessos: {sucessos}')
    print(f'Erros {erros}')
    print(f'Percentual de sucesso {percentual}')
    print(f'Classificacao {classificacao}')
    print('-'*30)
    print()
    if erros>maior_qtd_erros:
        maior_qtd_erros=erros
        endpoint_maior_erro=nome_endpoint
print(f'Endpoint com maior numero de erros {endpoint_maior_erro} - {maior_qtd_erros} erros')