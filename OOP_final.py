PAVADINIMAS_INDEX = 0
AUTORIUS_INDEX = 1
KAINA_INDEX = 2



def paieska():
    while True:
        f = open("knygynas.txt", 'r', encoding='utf-8')
        print("Iveskite savo pasirinkima: ")
        print("1. Ieskoti.")
        print("2. Rodyti visa biblioteka.")
        print("3. Baigti\n")

        pasirinkimas = input("Mano pasirinkimas: ")

        if pasirinkimas == '1':
            rastas = []
            paieska = input("Iveskite paieskos zodi (PVZ:autorius, kaina, pavadinimas): ")
            print()
            for line in f:
                if paieska.lower() in line.lower():
                    rastas.append(line.split('#')[PAVADINIMAS_INDEX])
                    print(line.split('#')[AUTORIUS_INDEX], "-",
                          line.split('#')[KAINA_INDEX], "-",
                          line.split('#')[PAVADINIMAS_INDEX])
            print()
            if len(rastas) == 0:
                print("Duomenu nerasta.\n")
        elif pasirinkimas == '2':
            for line in f:
                print(line.split('#')[AUTORIUS_INDEX], "-",
                      line.split('#')[KAINA_INDEX], "-",
                      line.split('#')[PAVADINIMAS_INDEX])
        elif pasirinkimas == '3':
            print("Baigiama.\n")
            break
        else:
            print("\nTokio pasirinkimo nera.\n")
        f.close()


def trinti_eilute():
    x = True
    trinama_eilute = 0
    while x:
        print("Pasirinkite kuria eilute norite trinti: \n1.Pirma.\n2.Paskutine.")
        pirma_paskutine = input("Iveskite pasirinkima: \n")

        if pirma_paskutine == '1':
            trinama_eilute = 0
            x = False
        elif pirma_paskutine == '2':
            trinama_eilute = -1
            x = False
        else:
            print("Klaidingas pasirinkimas.\n")

    textfile = open("knygynas.txt", "r+", encoding='utf-8')
    eiluciu_sarasas = []
    for eilute in textfile:
        eiluciu_sarasas.append(eilute)
    eiluciu_sarasas.pop(trinama_eilute)
    textfile.close()

    textfile = open("knygynas.txt", "w", encoding='utf-8')
    for eilute in eiluciu_sarasas:
        textfile.write(eilute)
    textfile.close()
    print("Eilute sekmingai istrinta.\n")

def trinti_pasirinkta_eilute():
    x = True
    while x:
        print("Spausdinti visa knygu sarasa?: ")
        spausdinti = input("Irasykite T(taip)/N(ne):")
        if spausdinti.lower() == "t" or spausdinti.lower() == "n":
            x = False
        else:
            print("Klaidingas pasirinkimas.\n")

    eilutes_index = 1
    textfile = open("knygynas.txt", "r+", encoding='utf-8')
    if spausdinti.lower() == "t":
        for line in textfile:
            print(eilutes_index,
                line.split('#')[AUTORIUS_INDEX], "-",
                line.split('#')[KAINA_INDEX], "-",
                line.split('#')[PAVADINIMAS_INDEX])
            eilutes_index +=1
        print()
    elif spausdinti.lower() == "n":
        pass
    textfile.close()

    x = True
    while x:
        trinama_eilute = input("Irasykite kuria eilute norite istrinti: ")
        if trinama_eilute.isdigit():
            trinama_eilute = int(trinama_eilute)
            x = False
        else:
            print("Prasome ivesti skaiciu.")

    textfile = open("knygynas.txt", "r+", encoding='utf-8')
    eiluciu_sarasas = []
    for eilute in textfile:
        eiluciu_sarasas.append(eilute)
    eiluciu_sarasas.pop(trinama_eilute-1)
    textfile.close()
    print("Sekmingai istrinta.\n")
    textfile = open("knygynas.txt", "w", encoding='utf-8')
    for eilute in eiluciu_sarasas:
        textfile.write(eilute)
    textfile.close()


def irasyti_duomenis():
    textfile = open("knygynas.txt", "a+")
    print("Duomenu ivedimo sablonas:")
    print("KNYGOS PAVADINIMAS#AUTORIUS#KAINA#")
    eilute = input('Iveskite duomenis: ')
    textfile.write("\n")
    textfile.write(eilute)
    textfile.close()
    print("Sekmingai irasyta: ", eilute, "\n")


def iterpti_duomenis():
    textfile = open("knygynas.txt", "r", encoding='utf-8')
    print("Duomenu ivedimo sablonas:")
    print("KNYGOS PAVADINIMAS#AUTORIUS#KAINA#")
    nauja_eilute_value = input('Iveskite duomenis: ')
    nauja_eilute_index = int(input("Eilutes numeris i kuria irasyti duomenis: "))
    tf = []
    for line in textfile:
        tf.append(line)
    textfile.close()
    tf.insert(nauja_eilute_index-1, nauja_eilute_value)
    tf.insert(nauja_eilute_index, "\n")
    print("Sekmingai ivesta.\n")
    textfile = open("knygynas.txt", "w", encoding='utf-8')
    for line in tf:
        textfile.write(line)
    textfile.close()


def spausdinti_biblioteka():
    textfile = open("knygynas.txt","r+", encoding='utf-8')
    eilutes_index = 1
    for line in textfile:
        print(eilutes_index,
                line.split('#')[AUTORIUS_INDEX], "-",
                line.split('#')[KAINA_INDEX], "-",
                line.split('#')[PAVADINIMAS_INDEX])
        eilutes_index +=1
    print()


def biblioteka_bubble():
    sarasas = []
    print("Rikiuoti pagal:")
    print("1. Knygos pavadinima.")
    print("2. Autoriu.")
    print("3. Kaina.")
    print()
    pasirinkimas = input("Iveskite savo pasirinkima: ")
    print()

    # Renkames pagal ka norime surusiuoti biblioteka.
    if pasirinkimas == '1':
        f = open("knygynas.txt", 'r', encoding='utf-8')
        for line in f:
            sarasas.append(line.split('#')[PAVADINIMAS_INDEX])
        f.close()
    elif pasirinkimas == '2':
        f = open("knygynas.txt", 'r', encoding='utf-8')
        for line in f:
            sarasas.append(line.split('#')[AUTORIUS_INDEX])
        sarasas = list(dict.fromkeys(sarasas))
        f.close()
    elif pasirinkimas == '3':
        f = open("knygynas.txt", 'r', encoding='utf-8')
        for line in f:
            sarasas.append(float(line.split('#')[KAINA_INDEX]))
        #Panaikinam dublikatus is saraso.
        sarasas = list(dict.fromkeys(sarasas))
        f.close()
    else:
        print("Klaidingas pasirinkimas.")
        print()

        # Bubble rusiavimo metodas
    indexing_lenght = len(sarasas) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_lenght):
            if sarasas[i] > sarasas[i + 1]:
                sorted = False
                sarasas[i], sarasas[i + 1] = sarasas[i + 1], sarasas[i]

    for pavadinimas in sarasas:
        print(pavadinimas)
    print("\n")
    return 0


while True:
    print("Pasirinkite funkcija: ")
    print("1.Paieska.\n2.Trinti pirma arba paskutine eilute.\n3.Trinti pasirinkta eilute.\n4.Irasyti duomenis i failo pabaiga."
          "\n5.Iterpti duomenis i faila.\n6.Spausdinti biblioteka.\n7.'Bubble' rusiavimas.\n8.Baigti.")
    ui = input("Jusu pasirinkimas:")

    if ui == '1':
        print("\n")
        paieska()
    elif ui == '2':
        print("\n")
        trinti_eilute()
    elif ui == '3':
        print("\n")
        trinti_pasirinkta_eilute()
    elif ui == '4':
        print("\n")
        irasyti_duomenis()
    elif ui == '5':
        print("\n")
        iterpti_duomenis()
    elif ui == '6':
        print("\n")
        spausdinti_biblioteka()
    elif ui == '7':
        print("\n")
        biblioteka_bubble()
    elif ui == '8':
        print("\nPrograma isjungiama.")
        break
    else:
        print("Tokio pasirinkimo nera. Kartokite.\n")

