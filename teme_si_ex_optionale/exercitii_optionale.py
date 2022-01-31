# Exercitiu 1:
lista = [2, 4, "mere", "banane", 4920, "Alex"]
lista.insert(5, "molotov")
lista.append("morcov")
print(lista)
# functia "append" adauga la sfarsitul listei noastre
# functia "insert" adauga un termen anume in locul din lista specificat de noi
# utilizare separata pentru insert
lista = [8, 5342, "portocala", 46, "elefant"]
lista.insert(3, "maimuta")
print(lista)
# append
lista = [954, "sampanie", -6549, 43, "barca"]
lista.append("sfarsit")
print(lista)

# Exerctiu 2:
propozitie = input("Introduceti propozitia: ")
total = 0

for a in propozitie:
    total = total + 1

print("Nr. total de caractere= ", total)
# ok