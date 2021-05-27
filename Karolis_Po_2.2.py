#Sukuriame zodyna
d = {'CK Hutchison Holdings Limited':'0001',
     'CLP Holdings Limited':'0002',
     'The Hong Kong and China Gas Company Limited':'0003',
     'The Wharf (Holdings) Limited': '0004',
     'HSBC Holdings plc': '0005'}
#Vartotojo paieskos ivestis
raktas = input('Iveskite raktini zodi: ')
rez = 0
#Randame kiek kiek gauname paieskos rezultatu. Jei neranda nieko palieka 0.
for i in d.keys():
    x = i.find(raktas)
    if(x != -1):
        rez+=1
#Ivedame kiek randame rezultatu, jei nerandame daugiau neisvadame nieko.
print("Rezultatu rasta:", rez)
if (rez == 0):
       print('Nerasta jokiu irasu')
print(100*"=")

#Naudojame ta pati for cikla tam kad galetume isvesti rastus rezultatus.
for i in d.keys():
    x = i.find(raktas)
    if(x != -1):
        print('{0:15} {1:35} {2:35}'.format(d.get(i), i, 'https://hk.finance.yahoo.com/quote/%s.HK' % d.get(i)))

        