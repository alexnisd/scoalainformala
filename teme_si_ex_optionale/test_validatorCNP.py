# aici era clar ca ne trebuie un input de la pers.
cnp = input('Introdu CNP-ul tau: ')
# m-am chinuit cu len-ul asta mai mult decat trebuia sincer
if len(cnp) != 13:
    print("Acest CNP nu are numarul corect de cifre")
    if cnp.isdigit() is False:
        print("Eu nu cred ca cnp-ul tau are litere")
else:
    s = cnp[0]  # sex
    a = cnp[1:3]  # an
    lun = cnp[3:5]  # luna
    z = cnp[5:7]  # zi
    j = cnp[7:9]  # judet
    n = cnp[9:12]  # jud, birouri de ev a pop, etc.
    c = cnp[-1]  # cifra da control
# verificam sa fie intr-un anumit interval
    sb = '1' <= s <= '9'  # de la 1 pana la 8 pt conationali iar 9 pt straini
    ab = '00' <= a <= '99'  # aici e destul de evident teoretic
    lb = '01' <= lun <= '12'  # la fel ca mai sus
    zb = '01' <= z <= '31'  # dap tot la fel ca mai sus
    jb = '01' <= j <= '52'   # aici la judet desigur cu exceptiile aferente(46, 51)
# '01': 'Alba', '02': 'Arad', '03': 'Arges', '04': 'Bacau', '05': 'Bihor', '06': 'Bistrita-Nasaud',
# '07': 'Botosani', '08': 'Brasov', '09': 'Braila', '10': 'Buzau', '11': 'Caras-Severin', '12': 'Cluj',
# '13': 'Constanta', '14': 'Covasna', '15': 'Dambovita', '16': 'Dolj', '17': 'Galati', '18': 'Gorj',
# '19': 'Harghita', '20': 'Hunedoara', '21': 'Ialomita', '22': 'Iasi', '23': 'Ilfov', '24': 'Maramures',
# '25': 'Mehedinti', '26': 'Mures', '27': 'Neamt', '28': 'Olt', '29': 'Prahova', '30': 'Satu-Mare',
# '31': 'Salaj', '32': 'Sibiu', '33': 'Suceava', '34': 'Teleorman', '35': 'Timis', '36': 'Tulcea',
# '37': 'Vaslui', '38': 'Valcea', '39': 'Vrancea', '40': 'Bucuresti', '41': 'Bucuresti Sector 1',
# '42': 'Bucuresti Sector 2', '43': 'Bucuresti Sector 3', '44': 'Bucuresti Sector 4',
# '45': 'Bucuresti Sector 5', '46': 'Bucuresti Sector 6', '51': 'Calarasi', '52': 'Giurgiu'
    nb = '001' <= n <= '999'  # jud, birouri de ev a pop, etc.
    if sb and ab and lb and zb and jb:
        print()
