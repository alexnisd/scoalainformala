import random


cnp = input("Introduceti CNP-ul: ")
n = len(cnp)
# s = sexul
# aa = anul
# ll = luna
# zz = ziua
# jj = judet
# nnn = judete si birouri
# c = cifra de control


def lungime():
    if n != 13:
        print("Acest CNP nu are numarul corect de litere")


lungime()


def alfanumeric():
    if cnp.isdigit():
        print("E ok ai scapat")
    else:
        print("Eu nu cred ca cnp-ul tau are litere bossule")


alfanumeric()


def sexul():




def anul():


def luna():


def ziua():


def cdc():


def jud():
    judet = {
            '01': 'Alba', '02': 'Arad', '03': 'Arges', '04': 'Bacau', '05': 'Bihor', '06': 'Bistrita-Nasaud',
            '07': 'Botosani', '08': 'Brasov', '09': 'Braila', '10': 'Buzau', '11': 'Caras-Severin', '12': 'Cluj',
            '13': 'Constanta', '14': 'Covasna', '15': 'Dambovita', '16': 'Dolj', '17': 'Galati', '18': 'Gorj',
            '19': 'Harghita', '20': 'Hunedoara', '21': 'Ialomita', '22': 'Iasi', '23': 'Ilfov', '24': 'Maramures',
            '25': 'Mehedinti', '26': 'Mures', '27': 'Neamt', '28': 'Olt', '29': 'Prahova', '30': 'Satu-Mare',
            '31': 'Salaj',
            '32': 'Sibiu', '33': 'Suceava', '34': 'Teleorman', '35': 'Timis', '36': 'Tulcea', '37': 'Vaslui',
           '38': 'Valcea', '39': 'Vrancea', '40': 'Bucuresti', '41': 'Bucuresti Sector 1', '42': 'Bucuresti Sector 2',
            '43': 'Bucuresti Sector 3', '44': 'Bucuresti Sector 4', '45': 'Bucuresti Sector 5',
            '46': 'Bucuresti Sector 6',
            '51': 'Calarasi', '52': 'Giurgiu'}
