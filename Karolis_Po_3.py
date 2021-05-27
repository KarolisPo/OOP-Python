import random #atsitiktiniu skaiciu modulis
import sys #funkciju ir metodu modulis

#sukuriame skaiciamo funkcija kuri skaiciuoja, bet pries tai patikrina ar ivesti skaiciai yra butent is 
#vartotojo sukurto saraso, jeigu skaicius ne is saraso programa pranesa ir issijungia.
def skaiciavimas():       
    num1 = float(input('Irasykite pirmaji skaiciu: '))
    tikrinimas_1 = sarasas.count(num1)
    if tikrinimas_1 !=1:
        print('Tokio skaiciaus sarase nera')
        sys.exit()
    num2 = float(input('Irasykite antraji skaiciu: '))
    tikrinimas_2 = sarasas.count(num2)
    if tikrinimas_2 !=1:
        print('Tokio skaiciaus sarase nera')
        sys.exit()
        
    if tikrinimas_1 == 1 and tikrinimas_2 == 1:
        op = input('Pasirinkite veiksma veiksma kuri norite atlikti: (+, -, *, / ): ')
        if op == '+':
            print(num1, '+', num2, '=', num1 + num2)
        elif op == '-':
            print(num1, '-', num2, '=', num1 - num2)
        elif op == '/':
            print(num1, '/', num2, '=', num1 / num2)
        elif op == '*':
            print(num1, '*', num2, '=', num1 * num2)
        else:
            print('Ivesties klaida')
            sys.exit()


#prasome vartotojo pasirinkti kokiu budu bus kuriamas sarasas.            
print('Generuoti skaicius automatiskai (A).\nRankinis skaiciu irasymas (R).')       
x = input('Iveskite pasirinkima: ')

if x.lower() == 'a':
    sarasas = [] #tuscias sarasas
    #pasirenkamas saraso dydis
    n = int(input("Iveskite kiek elementu bus sarase: ")) 
    print('Skaiciai generuojami atsitiktine tvarka')
    #naudodami for cikla sugeneruojame sarasa
    for i in range(0, n): 
        ele = float(random.randint(-25,25))
        sarasas.append(ele)
    print(sarasas) #isvedame sarasa
    skaiciavimas() #pradedame skaiciavimus
    
elif x.lower() == 'r':
    sarasas = [] 
  
    n = int(input("Iveskite kiek elementu bus sarase: ")) 
    print('Iveskite norimus elementus:')
    
    for i in range(0, n): 
        ele = float(input())
        sarasas.append(ele) 
    print('Jusu skaiciu saras yra:')
    print(sarasas)
    skaiciavimas()
else:
    print('Klaidingas pasirinkimas.')

