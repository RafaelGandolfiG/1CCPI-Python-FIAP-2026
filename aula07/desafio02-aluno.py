emails=dict()
email=input('digite os emails: ')
email=email.split(',')
email=tuple(email)
for i in email:
    nome,dominio=i.split('@')
    if dominio not in emails:
        emails[dominio]=1
    else:
        emails[dominio]+=1
print('quantidade de emails por dominio: ')
for i in emails:
    print(f'{i}: {emails[i]}')
print('lista de usuarios: ')
print(email)
print(f'primeiro usuario: {email[0]}')
print(f'ultimo email: {email[-1]}')
email=list(email)
email[-1],email[0]=email[0],email[-1]
email=tuple(email)
print('apos a troca de posições')
print(email)