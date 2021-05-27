print("Karolis Pociunas ISI-19I\n")

class Draugas:
    def __init__(self, vardas, ugis, svoris):
        self.vardas = vardas
        self.ugis = ugis
        self.svoris = svoris

    @classmethod
    def info(self):
        vardas = input("Iveskite vaikino varda: ")
        ugis = int(input("Iveskite vaikino ugi centimetrais: "))
        svoris = float(input("Iveskite vaikino svori kilogramais: "))
        return self(vardas, ugis, svoris)

    #funkcija kuri tikrina kurioje pozicijoje gali zaisti vaikinas.
    def kur_gali_zaisti(self):
        if self.ugis >= 180 and self.ugis <= 195:
            print(self.vardas, " gali zaisti gynejo arba izaidejo pozicijoje.")
        elif self.ugis > 195:
            print(self.vardas, " gali zaisti centro pozicijoje")
        else:
            print(self.vardas, " ugis nera tinkamas profesionaliam zaidimui.")

#ivedame duomenis apie kiekviena vaikina
vaikinas1 = Draugas.info()
vaikinas2 = Draugas.info()
vaikinas3 = Draugas.info()
vaikinas4 = Draugas.info()
#tikriname kur kiekvienas vaikinas gali zaisti
vaikinas1.kur_gali_zaisti()
vaikinas2.kur_gali_zaisti()
vaikinas3.kur_gali_zaisti()
vaikinas4.kur_gali_zaisti()