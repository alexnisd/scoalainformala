# Exercitiu 1
def sumanr(x, y, z):  # functie cum ne-ai cerut tu, cu x, y si z
    suma = x + y + z  # suma este egala cu x + y + z

    if x == y == z:  # practic aici if x y si z sunt egale le face suma * 3
        suma = suma * 3  # aici calculul pentru suma, adica cele 3 numere adunate * 3
    return suma  # aici returneaza suma


print(sumanr(16453534, 45534547644576, 7665745457), "<--- suma celor 3 numere daca nu sunt egale")
# aici ne alegem numerele diferite
print(sumanr(144444444456, 144444444456, 144444444456), "<--- suma celor 3 numere * 3 daca sunt egale")
# aici numerele la fel
# am incercat mai multe combinatii de numere sa vad daca pica codul, dar pana acum nu a picat
