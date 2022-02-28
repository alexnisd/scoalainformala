
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
        print("Acest CNP nu are numarul corect de cifre")


lungime()


def alfanumeric():
    if cnp.isdigit():
        print("Format ok")
    else:
        print("Eu nu cred ca cnp-ul tau are litere bossule")


alfanumeric()


def sexul():
    sexul = cnp[0]
    sexulbun = '1' <= sexul <= '9'
    if sexulbun:
        print("Sex ok")
    else:
        print('Mai uita-te la sex bro')


sexul()


def anul():
    anul = cnp[1:3]
    anulbun = '00' <= anul <= '99'
    if anulbun:
        print('An ok')
    else:
        print('An incorect')


anul()


def luna():
    luna = cnp[3:5]
    lunabuna = '01' <= luna <= '12'
    if lunabuna:
        print('Luna ok')
    else:
        print('Luna incorecta')


luna()


def ziua():
    ziua = cnp[5:7]
    ziuabuna = '01' <= ziua <= '31'
    if ziuabuna:
        print('Ziua ok')
    else:
        print('Zi incorecta')


ziua()


def judet():
    judet = cnp[7:9]
    judetbun = '01' <= judet <= '52'
    if judetbun:
        print('Judet ok')
    else:
        print('Judet incorect')


judet()


def nnn():
    nnn = cnp[9:12]
    nnnb = '001' <= nnn <= '999'
    if nnnb:
        print('nnn ok')
    else:
        print('nnn incorect')


nnn()


def cdc():
    cdc = cnp[-1]
    cdc = 0
    nr_control = '279146358279'
    for index, i in enumerate(cnp[:12]):
        cdc += int(i) * int(nr_control[index])
    cdc = cdc % 11
    if cdc == 10:
        cdc = 1
    cdc = cdc == int(cdc)
    if cdc:
        print('cdc ok')
    else:
        print('cdc incorect')


# if nnn and judet and ziua and luna and anul and sexul and alfanumeric and lungime:
if nnn and judet and ziua and luna and anul and sexul and alfanumeric and lungime and cdc:
    print("CNP ok!")
else:
    print('Nu-i ok :)')
