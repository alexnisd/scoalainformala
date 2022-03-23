# problema 1
# class Catalog:
#
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#         self. absente = 0
#         self.materii = {}
#
#     def __str__(self):
#         return f"{self.nume} {self.prenume} \n \t materii si note: {self.materii} \n \t absente: {self.absente}"
#
#     def increment_abs(self):
#         self.absente += 1
#
#     def delete_abs(self, numar_abs):
#         if self.absente >= numar_abs:
#             self.absente -= numar_abs
#
#
# class Extensie1(Catalog):
#     def __init__(self, nume, prenume):
#         super().__init__(nume, prenume)
#
#     def add_subject(self, materie, note):
#         self.materii.update({materie: note})
#
#     def print_all(self):
#         return f"{self.materii.keys()}"
#
#     def final_grade(self):
#
#         note_finale = {}
#         for i, j in self.materii.items():
#             for k in j:
#                 if all(isinstance(x, int) for x in j):
#                     medie = sum(j) / len(j)
#                     note_finale.update({i: medie})
#                 return note_finale
#
#
#
# student = Catalog("Roata", "ion")
# print(student)
# student.increment_abs()
# student.increment_abs()
# student.increment_abs()
# print(student)
# student.delete_abs(2)
# print(student)
#
# student2 = Catalog("Cerc", "George")
# student2.increment_abs()
# student2.increment_abs()
# student2.increment_abs()
# student2.increment_abs()
# student2.delete_abs(2)
# print(student2)
#
# obj = Extensie1("Ana", "Maria")
# obj.add_subject("Python", [5, 7, 8])
# obj.add_subject("Java", [3, 5, 7])
# obj.final_grade()
# print(obj.final_grade())

# problema 2

# from operator import itemgetter
#
# class Catalog_Prajituri:
#     lista_prajituri = []
#     def __init__(self, nume = "Chec", pret = 100, gramaj = 400):
#         self.nume = nume
#         self.pret = pret
#         self.gramaj = gramaj
#         caracteristici_obiect = [self.nume, self.pret, self.gramaj]
#         self.lista_prajituri.append(caracteristici_obiect)
#
#     @staticmethod
#     def sortare_pret():
#         sortata_pret = sorted(Catalog_Prajituri.lista_prajituri, key=itemgetter(1))
#         return f"Prajiturile sortate dupa pret sunt {sortata_pret}"
#
#     @staticmethod
#     def sortare_gramaj():
#         sortata_gramaj = sorted(Catalog_Prajituri.lista_prajituri, key=itemgetter(2))
#         return f"Prajiturile sortate dupa gramaj sunt {sortata_gramaj}"
#
# class Tort(Catalog_Prajituri):
#     def __init__(self, nume, gramaj, pret, etajat = False, glazura = "ciocolata"):
#         super().__init__(nume, gramaj, pret)
#         self.etajat = etajat
#         self.glazura = glazura
#
#     def __str__(self):
#         return f"Etajarea este {self.etajat} iar glazura este {self.glazura}"
#
# class Fursec(Catalog_Prajituri):
#     pass
#     # def __init__(self):
#     #     super().__init__()
#
# prj1=Catalog_Prajituri("Eclere", 10, 300)
# prj2=Catalog_Prajituri("Ecler mic", 7, 115)
# prj3=Catalog_Prajituri("Lava", 15, 275)
#
# tort1 = Tort(nume = "A", gramaj = 112, pret = 150, etajat = True, glazura = "cacao")
# tort2 = Tort(nume = "D", gramaj = 55, pret = 45, etajat = True, glazura = "cacao")
# tort3 = Tort(nume = "B", gramaj = 1150, pret = 350, etajat = True, glazura = "cacao")
#
# fursec1 = Fursec()
# # print(fursec1.nume)
#
# print(Catalog_Prajituri.lista_prajituri)
#
# print(Catalog_Prajituri.sortare_gramaj())
#
# # print(Catalog_Prajituri.sortare_pret())
#
#
# # print(tort1.glazura)
# # print(tort1.gramaj)
# # print(tort1.nume)
# #
# # print(tort1)

# class CatalogAuto:
#     def __init__(self, marca, tip):
#         self.marca = marca
#         self.tip = tip
#
#     def schimbare_culoare(self, culoare):
#         self.culoare = culoare
#
#     def __str__(self):
#         return f"Culoarea este: {self.culoare}"
#
#
# class ScauneIncalzite(CatalogAuto):
#     def __init__(self, scaune_incalzite, marca, tip):
#         super().__init__(marca, tip)
#         self.scaune_incalzite = scaune_incalzite
#
#     def __str__(self):
#         return f"Marca este: {self.marca}, Tipul este: {self.tip}, Scaune incalzite: {self.scaune_incalzite}"
#
#
# class BlocuriOpticeLED(CatalogAuto):
#     def __init__(self, blocuri_optice_led, marca, tip):
#         super().__init__(marca, tip)
#         self.blocuri_optice_led = blocuri_optice_led
#
#     def __str__(self):
#         return f"Marca este: {self.marca}, Tipul este: {self.tip}, Blocuri optice: {self.blocuri_optice_led}"
#
#
# obj = ScauneIncalzite(marca="Aro", tip=461, scaune_incalzite="Nu")
# print(obj)
# obj.schimbare_culoare("rosu")
# print(obj.culoare)
#
# obj2 = BlocuriOpticeLED(marca="Dacia", tip=1310, blocuri_optice_led="Nu")
# print(obj2)
# obj2.schimbare_culoare("negru")
# print(obj2.culoare)
# print(obj2.culoare, obj2.blocuri_optice_led, obj2.marca, obj2.tip)
# print(obj.culoare, obj.scaune_incalzite, obj.marca, obj.tip)

class Calcul:
    def __init__(self, a=1, b=2, c=3, d=4):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def verificare(self):
        self.e = f"Inf introduse nu sunt cifre"
        if str(self.a).isnumeric() and str(self.b).isnumeric() and str(self.c).isnumeric() and str(self.d).isnumeric():
            self.e = (self.a * (self.b + 3) / self.c) * self.d
        return self.e

    def __str__(self):
        return f"Rezult. este: {self.verificare()}"

obiect = Calcul()
print(obiect)
obiect2 = Calcul(5, 6, 7, 8)
print(obiect2)
obiect3 = Calcul("x", "y", "z", 2)
print(obiect3)
obiect4 = Calcul(9, 2)
print(obiect4)