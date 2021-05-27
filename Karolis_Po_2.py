
#Ivedame sveikaji skaiciu. Sukuriame tuscia sarasa. Naudodamiesi for ciklu atrenkame daliklius ir pridedame i tuscia sarasa.
#Spausdiname rezultata.
def dalikliai():
    num = int(input('Iveskite skaiciu: '))
    a=[]
    for x in range (1, num+1):
        if num%x == 0:
            a.append(x)
    print('Visi', num,'dalikliai yra: ')
    print(a)


# Sukuriame kintamuosius kuriu reiksmes kol kas yra nulines. Naudotojas iveda sakini. Naudojames for ciklu ir tikriname kiekviena sakinio simboli
# jeigu simbolis yra raide skaiciuojame +1 prie raidziu kintamojo, jeigu skaicius +1 prie skaiciaus kintamojo. Spausdiname programos rezultatus.
def simboliai():
    raides = 0
    skaiciai = 0
    eilute = input("Iveskite sakini: ")
 
    for i in eilute:
        if(i.isalpha()):
            raides = raides+1
        elif(i.isdigit()):
            skaiciai = skaiciai+1
          
    print('Jusu isvestame sakinyje yra', raides, 'raides.')
    print('Jusu ivestame sakinyje yra', skaiciai, 'skaiciai.')

#Sukuriamas tuscias sarasas. Naudotojui pateikiame uzklausa del saraso dydzio. Pasinaudodami for ciklu naudotojas suraso savo turima sarasa.
#Pasinaudoje fromkeys metodu pasaliname is vartotojo pateikto saraso dublikatus. Spausdinamas rezultatas.
def dublikatai():
    sarasas = [] 
  
    n = int(input("Iveskite kiek elementu bus sarase: ")) 
    print('Iveskite norimus elementus:')
    
    for i in range(0, n): 
        ele = input()
        sarasas.append(ele)
      
    sarasas = list(dict.fromkeys(sarasas))
    print('\nJusu elementu sarasas be dublikatu yra: ')
    print(sarasas)


#Uzklausa naudotojui pateikti savo sakini. Sukuriame tuscia zodyna. Isskaidome sakini i atskirus zodzius. Pasinaudoje for ciklu
#pridedami zodzius i zodyna, jeigu zodis pasikartoja prie zodyno reiksmes(key) "value" pridedam 1. Spausdiname rezultata.
def zodziu_sk():
    sakinys = input('Iveskite norima sakini: ')
    zodynas = dict()
    zodziai = sakinys.split()
    
    for i in zodziai:
        if i in zodynas:
            zodynas[i]+=1
        else:
            zodynas[i] =1
     
    print(zodynas)
    
x = True
#Sukuriame begalini cikla, pateikiamas programos meniu, programa reaguoja i galimus pasirinkimus ir kviecia atitinkamas
#funkcijas arba issijungia.
while x == True:
    print('\n')
    print('Sio programos funkcijos yra:')
    print('1.Visu pateikto skaiciaus dalikliu pateikimas.') 
    print('2.Sakinio raidziu ir skaiciu kiekio pateikimas.')
    print('3.Dublikatu salinimas is jusu pateikto saraso.')
    print('4.Zodziu skaiciavimas sakinyje.')
    print('5.Isjungti programa')
    
    y = int(input('Pasirinkite norima programos funkcija ivesdami jos numeri: '))
   
    if y == 1:
        dalikliai()
    elif y == 2:
        simboliai()
    elif y == 3:
        dublikatai()
    elif y == 4:
        zodziu_sk()
    elif y == 5:
        print('Programa isjungiama.')
        break
    else:
        print('Pasirinkimo klaida')
    
    
    
    
    
    
    
    