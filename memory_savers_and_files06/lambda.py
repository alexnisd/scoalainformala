# my_lambda = lambda x, y: x + y
# # denumire_functie = lambda param1, param2: corp_functie
# my_sum = my_lambda(2, 3)
# print(my_sum)
#
# def my_lambda(x, y):
#     return x + y

# diferenta = lambda x, y: x - y
# dif = diferenta(4, 3)
# print(dif)


players = [{
        "first_name": "Ion",
        "last_name" : "Gheorghe",
        "varsta": 12
    },
    {
        "first_name": "Andreea",
        "last_name": "Popa",
        "varsta": 15
    },
    {
        "first_name": "Andrei",
        "last_name": "Alea",
        "varsta": 19
    }
]

jucatori_sortati = sorted(players, key=lambda player: player["varsta"])
print(jucatori_sortati)