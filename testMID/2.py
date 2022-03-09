# Exercitiul 2
def prnt3(lista):  # am facut si cu functie asa cum ne-ai rugat :)))
  pozitie = 3 - 1  # aici practic am pus ca si pozitie 3 - 1 ca sa dea 2 pentru ca incepem teoretic sa scoatem de la 2
# daca numaratoarea incepe de la 0
  index = 0  # index pt ca indexul e 0 teoretic incepem de la 0 (1 fiind 0)
  lungime = (len(lista))  # aici am pus un len pentru lungimea listei
# aici am facut un while ca sa se opreasca codul cand lista devine goala / cand nu mai sunt numere de scos
  while lungime > 0:  # aici am pus un while atat timp cat lungimea listei este mai mare ca 0
    index = (pozitie + index) % lungime  # aici un mic calcul care sa imparta pozitia si indexul la lungime
    print(lista.pop(index))  # practic aici am pus un pop de index ca sa scoata din lista o valoare si dupa sa o
# returneze
    lungime -= 1  # practic aici am pus lungime de -= scadea din lungimea listei cu 1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # aici avem lista de numere data de exercitiu
print(f"Lista inainte de remove: {nums}")  # aici am dat un print ca sa se vada lista inainte de remove
prnt3(nums)  # aici practic am apelat
print(f"Lista dupa remove: {nums} <--- e cam gol pe aici :)) ")  # aici am dat print dupa remove teoretic
