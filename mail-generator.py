import json
from random import randint
from pprint import pprint

providers = ['@gmail.com', '@outlook.com', '@yahoo.com', '@protonmail.com', '@zoho.eu', '@mail.com', '@gmx.com', '@mailbox.org']

with open('names.json', encoding='utf-8') as f:
    data = json.load(f)

with open('surnames.json', encoding='utf-8') as surdata:
    surnames = json.load(surdata)


mail = list()
for i in range(400):
    mail.append(str(data[randint(0,len(data)-1)]) + str(surnames[randint(0,len(surnames)-1)]) + str(randint(00,99)) + providers[randint(0,len(providers)-1)])


with open('mail.json', 'w', encoding='utf-8') as w:
    json.dump(mail , w, sort_keys=True, ensure_ascii=False, indent=0)
pprint(mail)
