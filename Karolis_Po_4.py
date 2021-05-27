
import string
import collections

#Funkcija skirta skaiciuoti teksto simbolius pasinaudojant for loop.
def simboliai():
    textfile = open("tekstas.txt", "r+")
    raides = 0
    skaiciai = 0
    kiti = 0
    eilute = textfile.read()


    for i in eilute:
        if(i.isalpha()):
            raides = raides+1
        elif(i.isdigit()):
            skaiciai = skaiciai+1
        else:
            kiti = kiti+1
          
    print('Siame tekste yra:', raides, 'raides,', skaiciai, 'skaiciai ir',kiti, 'kiti simboliai.')
    textfile.close()
    
    
#Funkcija leidzia irasyti norima teksta ir failo pabaiga.  
def prideti():
    textfile = open("tekstas.txt", "a+")
    eilute = input('Iveskite sakini ar zodi kuri norite irasyti sio failo gale: ')
    textfile.write(eilute)
    textfile.close()

#Funkcija kuri uzkoduoja teksta per vartotojo irasyta poslinki.
def ceaser(rotate_string, number_to_rotate_by):  #kviesdami funkcija nurodome teksta ir poslinki
    #sukuriame didziuju ir mazuju raidziu sarasus
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    #pasukame sukurta sarasa nurodytu poslinkiu
    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)
    #sarasa paverciame eilute
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    #perkeliame teksto simbolius tokia tvarka kokia buvo nustumti pradiniai raidziu sarasai
    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))

#Menu. Kvieciamos atitinkamos funkcijos pagal vartotojo irasyta pasirinkima.
x = True
while x == True:
    print("\n")
    print ('Pasirinkite norima funkcija:\n 1.Irasyti savo teksta i failo pabaiga. \n 2.Spausdinti teksta. \n 3.Koduoti teksta. \n 4.Spausdinti koduota teksta. \n 5.Sifruoti teksta. \n 6.Skaiciuoti teksto simbolius, raides ir skaicius \n 7.Baigti.')
    pasirinkimas = input('Irasykite funkcijos numeri: ')
    print("\n")

    if pasirinkimas == '1':
        prideti()
    elif pasirinkimas == '2':
        textfile = open("tekstas.txt", "r")
        print(textfile.read())
        textfile.close()
    elif pasirinkimas == '3':
        a = int(input('Iveskite per kiek simboliu atliekamas postumis: '))
        text = open("tekstas.txt", "r+")
        eilute = text.read()
        ceaser(eilute, a)
        ceaser_text = ceaser(eilute, a)
        text.close()
        with open ('sifruotas_tekstas.txt', 'w') as st:
            st.write(ceaser_text)
            st.close()
            text.close()
    elif pasirinkimas == '4':
        st = open("sifruotas_tekstas.txt", "r")
        print(st.read())
        st.close()
    elif pasirinkimas == '5':
        b = int(input('Irasykite per kiek simboliu buvo atliktas postumis: '))
        text = open("sifruotas_tekstas.txt", "r")
        eilute = text.read()
        normal_text = ceaser(eilute, -b)
        print(normal_text)
        text.close()
    elif pasirinkimas == '6':
        simboliai()
    elif pasirinkimas == '7':
        print('Baigiama.')
        break
    else:
        print('Klaidingas pasirinkimas.')
    

