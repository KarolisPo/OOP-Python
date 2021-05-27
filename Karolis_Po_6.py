#klase Draugas nurodo kokius duomenis turesime apie drauga ir kviecia funkcija kuri priskiria tuos duomenis
class Draugas:
    def __init__(self, vardas, ugis, svoris):
        self.vardas = vardas
        self.ugis = ugis
        self.svoris = svoris

    #sis metodas padeda priskirti duomenis konkreciam objektui
    @classmethod
    def info(self):
        vardas = input("Iveskite vaikino varda: ")
        ugis = int(input("Iveskite vaikino ugi centimetrais: "))
        svoris = float(input("Iveskite vaikino svori kilogramais: "))
        return self(vardas, ugis, svoris)

#duomenu priskirimas konkreciam objektui
vaikinas1 = Draugas.info()
vaikinas2 = Draugas.info()
vaikinas3 = Draugas.info()
vaikinas4 = Draugas.info()

draugu_sarasas = [vaikinas1, vaikinas2, vaikinas3, vaikinas4]
ugis = []

#visus esamonius ugius sudedame i sarasa
for vaikinas in draugu_sarasas:
    ugis.append(vaikinas.ugis)
#isvedame vaikina su maziausiu ugiu
for vaikinas in draugu_sarasas:
    if min(ugis) == vaikinas.ugis:
        print("Zemiausias vaikinas yra: ", vaikinas.vardas, " jo ugis - ", vaikinas.ugis)
#issivedame bendra visu vaikinu svori
pradinis_svoris = 0
for vaikinas in draugu_sarasas:
    pradinis_svoris +=vaikinas.svoris

svorio_vidurkis = pradinis_svoris / len(draugu_sarasas)

print("Draugu svorio vidurkis yra: ", svorio_vidurkis)



