# def validate_cnp(field):
#     if field.data.isdigit():
#         if len(field.data) != 13:
#             raise ValidationError('CNP-ul trebuie sa aiba 13 caractere!')
#         if field.data.startswith('0'):
#             raise ValidationError('CNP-ul nu poate sa inceapa cu cifra 0.')
#         cnp_check = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
#         k = 0
#         for i in range(0, len(cnp_check)):
#             k += int(field.data[i]) * int(cnp_check[i])
#         if k % 11 == int(field.data[12]):
#             return True
#         elif k % 11 == 10 and int(field.data[12]) == 1:
#             return True
#         else:
#             raise ValidationError('CNP-ul introdus {} nu este valid.'.format(field.data))
#     else:
#         raise ValidationError('CNP-ul trebuie sa contina doar cifre!')
#
#
# # s este un dictionar care contine sexul, cetatenia si secolul nasterii, in functie de prima cifra a CNP-ului
# status = {
#     1: ('masculin', 'roman', 19), 2: ('feminin', 'roman', 19), 3: ('masculin', 'roman', 18),
#     4: ('feminin', 'roman', 18), 5: ('masculin', 'roman', 20), 6: ('feminin', 'roman', 20),
#     7: ('masculin', 'rezident', ''), 8: ('feminin', 'rezident', ''), 9: ('', 'strain', '')
# }
# # l este un dictionar care contine lunile anului
# luna = {
#     '01': 'ianuarie', '02': 'februarie', '03': 'martie', '04': 'aprilie', '05': 'mai', '06': 'iunie',
#     '07': 'iulie', '08': 'august', '09': "septembrie", '10': 'octombrie', '11': 'noiembrie', '12': 'decembrie'
# }
# # j este un dictionar care contine judetele si codul loc corespondent
# judet = {
#     '01': 'Alba', '02': 'Arad', '03': 'Arges', '04': 'Bacau', '05': 'Bihor', '06': 'Bistrita-Nasaud',
#     '07': 'Botosani', '08': 'Brasov', '09': 'Braila', '10': 'Buzau', '11': 'Caras-Severin', '12': 'Cluj',
#     '13': 'Constanta', '14': 'Covasna', '15': 'Dambovita', '16': 'Dolj', '17': 'Galati', '18': 'Gorj',
#     '19': 'Harghita', '20': 'Hunedoara', '21': 'Ialomita', '22': 'Iasi', '23': 'Ilfov', '24': 'Maramures',
#     '25': 'Mehedinti', '26': 'Mures', '27': 'Neamt', '28': 'Olt', '29': 'Prahova', '30': 'Satu-Mare', '31': 'Salaj',
#     '32': 'Sibiu', '33': 'Suceava', '34': 'Teleorman', '35': 'Timis', '36': 'Tulcea', '37': 'Vaslui',
#     '38': 'Valcea', '39': 'Vrancea', '40': 'Bucuresti', '41': 'Bucuresti Sector 1', '42': 'Bucuresti Sector 2',
#     '43': 'Bucuresti Sector 3', '44': 'Bucuresti Sector 4', '45': 'Bucuresti Sector 5', '46': 'Bucuresti Sector 6',
#     '51': 'Calarasi', '52': 'Giurgiu'
# }
#
#
# # import random
# # def CNP():
# #     user_input = input("Introduceti CNP: ")
# #
# #     tup_1 = user_input[0]
# #     tup_2 = user_input[1:3]
# #     tup_3 = user_input[3:5]
# #     tup_4 = user_input[5:7]
# #     tup_5 = user_input[7:9]
# #     tup_6 = user_input[9:12]
# #     tup_7 = user_input[-1]
# #
# #     tup_1_verified = "1" <= tup_1 <= "9"
# #     tup_2_verified = "00" <= tup_2 <= "99"
# #     tup_3_verified = "01" <= tup_3 <= "12"
# #     tup_4_verified = "01" <= tup_4 <= "31"
# #     tup_5_verified = "01" <= tup_5 <= "51"
# #     tup_6_verified = "001" <= tup_6 <= "999"
# #
# #     c_intup = 0
# #     ex_numar = '279146358279'
# #     for intup, anyin in enumerate(user_input[:12]):
# #         c_intup += int(anyin) * int(ex_numar[intup])
# #     c_intup = c_intup % 11
# #     if c_intup == 10:
# #         c_intup = 1
# #     tup_7_verified = c_intup == int(tup_7)
# #
# #     if len(user_input) == 13 \
# #             and tup_1_verified \
# #             and tup_2_verified \
# #             and tup_3_verified \
# #             and tup_4_verified \
# #             and tup_5_verified \
# #             and tup_6_verified \
# #             and tup_7_verified:
# #         print("CNP-ul introdus este valid!")
# #     else:
# #         print("CNP-ul introdus este invalid")
# #
# # CNP()
#
# import random
#
# print("Validator CNP")
#
#
# def cnp():
#     sexul = int
# def sexul():
#
#     sexul = str(input("Introduceti sexul(masculin/feminin): "))
#
# def anul_nasterii():
#
#     anul_nasterii = int(input("Introduceti ultimele 2 cifre in anul nasterii: "))
#
# def luna_nasterii():
#     luna_nasterii = input("Introduceti luna nasterii: ")
#
# def ziua_nasterii():
#     ziua_nasterii = input("Introduceti ziua nasterii: ")
#
# def judetul():
#     judetul_inp = input("Introduceti judetul: ")
#
#     if sexul == "masculin":
#         s = 1
#     else:
#         s = 2
#
#     if 00 <= int(anul_nasterii) <= 99:
#         aa = anul_nasterii
#
#     if 1 <= int(luna_nasterii) <= 12:
#         ll = luna_nasterii
#
#     if 1 <= int(ziua_nasterii) <= 31:
#         zz = ziua_nasterii
#
#     judet = {1: "alba",
#              2: "arad",
#              3: "arges",
#              4: "bacau",
#              5: "bihor",
#              6: "bistrita-nasaud",
#              7: "botosani",
#              8: "brasov",
#              9: "braila",
#              10: "buzau",
#              11: "caras-severin",
#              12: "cluj",
#              13: "constanta",
#              14: "covasna",
#              15: "dambovita",
#              16: "dolj",
#              17: "galati",
#              18: "gorj",
#              19: "harghita",
#              20: "hunedoara",
#              21: "ialomita",
#              22: "iasi",
#              23: "ilfov",
#              24: "maramures",
#              25: "mehedinti",
#              26: "mures",
#              27: "neamt",
#              28: "olt",
#              29: "prahova",
#              30: "satu mare",
#              31: "salaj",
#              32: "sibiu",
#              33: "suceava",
#              34: "teleorman",
#              35: "timis",
#              36: "tulcea",
#              37: "vaslui",
#              38: "valcea",
#              39: "vrancea",
#              40: "bucuresti",
#              41: "bucuresti s.1",
#              42: "bucuresti s.2",
#              43: "bucuresti s.3",
#              44: "bucuresti s.4",
#              45: "bucuresti s.5",
#              46: "bucuresti s.6",
#              51: "calarasi",
#              52: "giurgiu"}
#
#     judet_key = judet
#     judet_listin = list(judet_key)
#     judet_valori = judet.values()
#     judet_lista = list(judet_valori)
#
#     if judetul_inp in judet_lista:
#         index = judet_lista.index(Judet)
#         jj = judet_listin[index]
#
# cnp()

phNo = input("Enter the phone number: ")
length = len(phNo)
if length == 12 \
    and phNo[3] == "-" \
    and phNo[7] == "-" \
    and phNo[:3].isdigit() \
    and phNo[4:7].isdigit() \
    and phNo[8:].isdigit() :
    print("Valid Phone Number")
else :
    print("Invalid Phone Number")