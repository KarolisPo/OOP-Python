#Pasinaudoje matematine formule sukuriame funkcija kuri apskaiciuoja pirmuju n skaiciu suma.
def suma():
    n = int(input('Iveskite sveikaji skaiciu: '))
    result = (n * (n + 1)) / 2
    print('Pirmuju',n,'skaiciu suma yra:',result)
    
#Prasome naudotojo ivesti laipsnius pagal celsijaus skale ir pasinaudoje matematine formule 
#convertuojame laipsnius pagal celsiju i farenheito laipsnius
def termometras():
    celsijus = float(input('Iveskite laipsnius pagal celsijau skale: '))
    result = (celsijus * 1.8) + 32
    print(celsijus,'laipsniai pagal Celsiju atitinka',result,'Farenheito laipsnius.')
    
#Prasome naudotojo ivesti akcijos koda, pasinaudoje matematine logika teisingu ivesties variantu pateikiame
#akcijos URL, jeigu kodas per ilgas arba per trumpas nurodome naudotojui, jog padare ivesties klaida.
def url():
    akcija = input('Iveskite akcijos koda: ')
    if len(akcija) == 4:
        print('Akcija bus suteikta paspaudus sia nuoroda:')
        print('https://hk.finance.yahoo.com/quote/',akcija,'.HK ',sep="")
    if len(akcija) > 4 or len(akcija) < 4 :
        print('Ivesties klaida. Akcijos kodas per ilgas')
    
#Vartotojo ivesta sakini isskaidom i atskirus zodzius, pasinaudoje reversed() sukeiciame zodzius vietomis,
#vel sujungiame zodzius sudedami tarpus tarp ju ir juos atspausdiname.
def kita_puse():
    sakinys =input("Iveskite sakini: ")
    zodziai = sakinys.split()
    zodziai = list(reversed(zodziai))
    print('\nJusu ivestas sakinys is kitos puses yra: ')
    print(" ".join(zodziai))
    
#Naudodojas iveda informacija apie savo biudzeta bei mokescius, bulio algebros pagalba programa reaguoja i vartotojo atsakymus
#ir pateikia atitinkamus skaiciavimus. Spausdinamas galutinis biudzeto likutis menesio gale.
def biudzetas():
    pajamos = float(input('Iveskite seimos menesio pajamas: '))
    mokesciai = float(input('Iveskite kiek sumokesite mokesciu: '))
    maistas = float(input('Iveskite kiek isleisite maistui: '))
    extra = input('Nurodykite ar bus papildomu islaidu TAIP(T)/NE(N):')
    
    if extra.lower() == 't':
        islaidos_kaina = float(input('Kiek isleisite papildomai?: '))
    elif extra.lower() == 'n':
        print('Papildomu islaidu nebus')
        islaidos_kaina = 0
    else:
        print('Pasirinkimo klaida')
        islaidos_kaina = 0
        
    biudzeto_likutis = pajamos - (mokesciai + maistas + islaidos_kaina)
    print('Gale menesio Jusu biudzeto likutis bus:', biudzeto_likutis )
    

x = True
#Sukuriame begalini cikla, pateikiamas programos meniu, programa reaguoja i galimus pasirinkimus ir kviecia atitinkamas
#funkcijas arba issijungia.
while x == True:
    print('\n')
    print('Sio programos funkcijos yra:')
    print('1.Pirmuju n teigiamu skaiciu sumos skaiciavimas.') 
    print('2.Laipsniu keitimas is celsijaus skales i farengeito.')
    print('3.Akcijos URL generavimas.')
    print('4.Sakinio/zodzio pakeitimas i atbuline tvarka.')
    print('5.Menesinio biudzeto skaiciavimas.')
    print('6.Isjungti programa')
    
    y = int(input('Pasirinkite norima programos funkcija ivesdami jos numeri: '))
   
    if y == 1:
        suma()
    elif y == 2:
        termometras()
    elif y == 3:
        url()
    elif y == 4:
        kita_puse()
    elif y == 5:
        biudzetas()
    elif y == 6:
        print('Programa isjungiama.')
        break
    else:
        print('Pasirinkimo klaida')
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          