#nurodome kad kiekviena plyta turi ilgi ploti ir auksti
class plyta:
    def __init__(self, ilgis, plotis, aukstis):
        self.ilgis = ilgis
        self.plotis = plotis
        self.aukstis = aukstis

#pasinaudodami klase priskiriame reiksmes konkreciam objektui
plyta_1 = plyta(0.25, 0.16, 0.065)
plyta_2 = plyta(0.25, 0.12, 0.088)

#funkcija kuri skaiciuoja pirmajai sienai reikalinga plytu skaiciu
def pirmas_sluoksnis():
    plytu_skaicius_sienai1 = round((sienos_aukstis_1 * sienos_ilgis_1) / (plyta_1.aukstis * plyta_1.ilgis))
    plytu_skaicius_sienai2 = round((sienos_aukstis_2 * sienos_ilgis_2) / (plyta_1.aukstis * plyta_1.ilgis))
    plytu_skaicius_sienai3 = round((sienos_aukstis_3 * sienos_ilgis_3) / (plyta_1.aukstis * plyta_1.ilgis))
    plytu_skaicius_sienai4 = round((sienos_aukstis_4 * sienos_ilgis_4) / (plyta_1.aukstis * plyta_1.ilgis))
    print("Plytos aukstis: ", plyta_1.aukstis)
    print("Plytos ilgis: ", plyta_1.ilgis)
    print("Plytos plotis: ", plyta_1.plotis)
    print()
    print("Pirmos rusies plytu pirmai sienai reikes: ", plytu_skaicius_sienai1)
    print("Pirmos rusies plytu antrai sienai reikes: ", plytu_skaicius_sienai2)
    print("Pirmos rusies plytu treciai sienai reikes: ", plytu_skaicius_sienai3)
    print("Pirmos rusies plytu ketvirtai sienai reikes: ", plytu_skaicius_sienai4)

#funkcija kuri skaiciuoja antrajai sienai reikalinga plytu skaiciu
def antras_sluoksnis():
    plytu_skaicius_sienai1 = round((sienos_aukstis_1 * sienos_ilgis_1) / (plyta_2.aukstis * plyta_2.ilgis))
    plytu_skaicius_sienai2 = round((sienos_aukstis_2 * sienos_ilgis_2) / (plyta_2.aukstis * plyta_2.ilgis))
    plytu_skaicius_sienai3 = round((sienos_aukstis_3 * sienos_ilgis_3) / (plyta_2.aukstis * plyta_2.ilgis))
    plytu_skaicius_sienai4 = round((sienos_aukstis_4 * sienos_ilgis_4) / (plyta_2.aukstis * plyta_2.ilgis))
    print("Plytos aukstis: ", plyta_2.aukstis)
    print("Plytos ilgis: ", plyta_2.ilgis)
    print("Plytos plotis: ", plyta_2.plotis)
    print()
    print("Antros rusies plytu pirmai sienai reikes: ", plytu_skaicius_sienai1)
    print("Antros rusies plytu antrai sienai reikes: ", plytu_skaicius_sienai2)
    print("Antros rusies plytu treciai sienai reikes: ", plytu_skaicius_sienai3)
    print("Antros rusies plytu ketvirtai sienai reikes: ", plytu_skaicius_sienai4)

#paskaiciuojame sienu stori
def sienos_storis():
    storis = plyta_1.plotis + plyta_2.plotis
    print("Sienu storis: ", storis)

#vartotojas isiveda sienu matmenis
sienos_aukstis_1 = float(input("Iveskite pirmos sienos auksti metrais: "))
sienos_ilgis_1 = float(input("Iveskite pirmos sienos ploti metrais: "))
print()
sienos_aukstis_2 = float(input("Iveskite antros sienos auksti metrais: "))
sienos_ilgis_2 = float(input("Iveskite antros sienos ploti metrais: "))
print()
sienos_aukstis_3 = float(input("Iveskite trecios sienos auksti metrais: "))
sienos_ilgis_3 = float(input("Iveskite trecios sienos ploti metrais: "))
print()
sienos_aukstis_4 = float(input("Iveskite ketvirtos sienos auksti metrais: "))
sienos_ilgis_4 = float(input("Iveskite ketvirtos sienos ploti metrais: "))
print()

pirmas_sluoksnis()
print()
antras_sluoksnis()
sienos_storis()
