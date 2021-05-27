# pasizymime indexus kuriu nekeisime
VARDAS_INDEX = 0
PAVARDE_INDEX = 1
METAI_INDEX = 2
UGIS_INDEX = 3


# klase skirti saugoti zaidejo duomenims
class Krepsininkas:
    def __init__(self, vardas, pavarde, amzius, ugis):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        self.ugis = ugis


vilniaus_zaidejai = []


# is failo traukiame duomenis ir kuriame objektu sarasa
def duomenys_vilnius():
    textfile = open("krepsinis_1.txt", "r+", encoding='utf-8')
    for line in textfile:
        vilniaus_zaidejai.append(Krepsininkas(line.split('#')[VARDAS_INDEX], line.split('#')[PAVARDE_INDEX],
                                              line.split('#')[METAI_INDEX], line.split('#')[UGIS_INDEX]))
    vilniaus_zaidejai.pop(0)


kauno_zaidejai = []

# is failo traukiame duomenis ir kuriame objektu sarasa
def duomenys_kaunas():
    textfile = open("krepsinis_2.txt", "r+", encoding='utf-8')
    for line in textfile:
        kauno_zaidejai.append(Krepsininkas(line.split('#')[VARDAS_INDEX], line.split('#')[PAVARDE_INDEX],
                                           line.split('#')[METAI_INDEX], line.split('#')[UGIS_INDEX]))
    kauno_zaidejai.pop(0)

# naudodamiesi klases objektu sarasu randame zaideju amziaus ir ugio vidurkis
def ugio_amziaus_vidurkis_vilnius():
    bendras_ugis = 0
    bendras_amzius = 0
    vaikinu_sk = 0
    for zaidejas in vilniaus_zaidejai:
        bendras_ugis += int(zaidejas.ugis)
        bendras_amzius += int(zaidejas.amzius)
        vaikinu_sk += 1
    ugio_vidurkis = round(bendras_ugis / vaikinu_sk, 1)
    amziaus_vidurkis = round(bendras_amzius / vaikinu_sk, 1)
    return ugio_vidurkis, amziaus_vidurkis

# naudodamiesi klases objektu sarasu randame zaideju amziaus ir ugio vidurkis
def ugio_amziaus_vidurkis_kaunas():
    bendras_ugis = 0
    bendras_amzius = 0
    vaikinu_sk = 0
    for zaidejas in kauno_zaidejai:
        bendras_ugis += int(zaidejas.ugis)
        bendras_amzius += int(zaidejas.amzius)
        vaikinu_sk += 1
    ugio_vidurkis = round(bendras_ugis / vaikinu_sk, 1)
    amziaus_vidurkis = round(bendras_amzius / vaikinu_sk, 1)
    return ugio_vidurkis, amziaus_vidurkis

# naudodamiesi klases objektu sarasais randame auksciausia zaideja Vilniuje ir Kaune
def auksciausias():
    auksciausias_vilniuje = 0
    for zaidejas in vilniaus_zaidejai:
        if int(zaidejas.ugis) > auksciausias_vilniuje:
            auksciausias_vilniuje = int(zaidejas.ugis)
    for zaidejas in vilniaus_zaidejai:
        if int(zaidejas.ugis) == auksciausias_vilniuje:
            print("Auksciausias zaidejas Vilniuje yra:", zaidejas.vardas, zaidejas.pavarde, "-", zaidejas.ugis, "cm")

    auksciausias_kaune = 0
    for zaidejas in kauno_zaidejai:
        if int(zaidejas.ugis) > auksciausias_kaune:
            auksciausias_kaune = int(zaidejas.ugis)
    for zaidejas in kauno_zaidejai:
        if int(zaidejas.ugis) == auksciausias_kaune:
            print("Auksciausias zaidejas Kaune yra:", zaidejas.vardas, zaidejas.pavarde, "-", zaidejas.ugis, "cm")

    if auksciausias_vilniuje > auksciausias_kaune:
        print("Auksciausias zaidejas yra Vilniaus krepsinio mokykloje.")
    else:
        print("Auksciausias zaidejas yra Kauno krepsinio mokykloje.")

# indeksuojant funkcija kurioje skaiciavome amziaus ir ugio vidurki imame rasta ugio vidurki is vienos ir kitos krepsinio
# mokyklos ir sulygine isvedame zaidejus kurie yra aukstesni uz vidurki
def didesnis_uz_vidurki():
    vilniaus_ugio_vidurkis = ugio_amziaus_vidurkis_vilnius()[0]
    print("\nVilniaus zaidejai kuriu amzius yra didesnis uz vidurki:")
    for zaidejas in vilniaus_zaidejai:
        if float(zaidejas.ugis) > vilniaus_ugio_vidurkis:
            print(zaidejas.vardas, zaidejas.pavarde, "-", zaidejas.ugis, "cm")

    kauno_ugio_vidurkis = ugio_amziaus_vidurkis_kaunas()[0]
    print("\nKauno zaidejai kuriu amzius yra didesnis uz vidurki:")
    for zaidejas in kauno_zaidejai:
        if float(zaidejas.ugis) > kauno_ugio_vidurkis:
            print(zaidejas.vardas, zaidejas.pavarde, "-", zaidejas.ugis, "cm")


duomenys_kaunas()
duomenys_vilnius()
ugio_amziaus_vidurkis_vilnius()
ugio_amziaus_vidurkis_kaunas()

print("Kauno zaideju ugio vidurkis yra:", ugio_amziaus_vidurkis_kaunas()[0], "cm.")
print("Kauno zaideju amzius vidurkis yra:", ugio_amziaus_vidurkis_kaunas()[1], "m.\n")
print("Vilniaus zaideju ugio vidurkis yra:", ugio_amziaus_vidurkis_vilnius()[0], "cm.")
print("Vilniaus zaideju amzius vidurkis yra:", ugio_amziaus_vidurkis_vilnius()[1], "m.\n")

auksciausias()
didesnis_uz_vidurki()
