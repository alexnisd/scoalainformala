import random

print("Validator CNP")


def cnp():

    global s, aa, ll, zz, jj, nnn, c, z

    sexul = str(input("Introduceti sexul(masculin/feminin): "))

    anul_nasterii = int(input("Introduceti ultimele 2 cifre in anul nasterii: "))

    luna_nasterii = input("Introduceti luna nasterii: ")

    ziua_nasterii = input("Introduceti ziua nasterii: ")

    judetul_inp = input("Introduceti judetul: ")

    if sexul == "masculin":
        s = 1
    else:
        s = 2

    if 00 <= int(anul_nasterii) <= 99:
        aa = anul_nasterii

    if 1 <= int(luna_nasterii) <= 12:
        ll = luna_nasterii

    if 1 <= int(ziua_nasterii) <= 31:
        zz = ziua_nasterii

    judet = {1: "alba",
             2: "arad",
             3: "arges",
             4: "bacau",
             5: "bihor",
             6: "bistrita-nasaud",
             7: "botosani",
             8: "brasov",
             9: "braila",
             10: "buzau",
             11: "caras-severin",
             12: "cluj",
             13: "constanta",
             14: "covasna",
             15: "dambovita",
             16: "dolj",
             17: "galati",
             18: "gorj",
             19: "harghita",
             20: "hunedoara",
             21: "ialomita",
             22: "iasi",
             23: "ilfov",
             24: "maramures",
             25: "mehedinti",
             26: "mures",
             27: "neamt",
             28: "olt",
             29: "prahova",
             30: "satu mare",
             31: "salaj",
             32: "sibiu",
             33: "suceava",
             34: "teleorman",
             35: "timis",
             36: "tulcea",
             37: "vaslui",
             38: "valcea",
             39: "vrancea",
             40: "bucuresti",
             41: "bucuresti s.1",
             42: "bucuresti s.2",
             43: "bucuresti s.3",
             44: "bucuresti s.4",
             45: "bucuresti s.5",
             46: "bucuresti s.6",
             51: "calarasi",
             52: "giurgiu"}

    judet_key = judet
    judet_listin = list(judet_key)
    judet_valori = judet.values()
    judet_lista = list(judet_valori)

    if judetul_inp in judet_lista:
        index = judet_lista.index(Judet)
        jj = judet_listin[index]
    return "CNP valid"

cnp()

