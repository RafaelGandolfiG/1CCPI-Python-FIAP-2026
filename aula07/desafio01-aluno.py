emails=dict()
email=input('digite os emails: ')
email=email.split(',')
for i in email:
    nome,dominio=i.split('@')
    if dominio not in emails:
        emails[dominio]=1
    else:
        emails[dominio]+=1
print(emails)