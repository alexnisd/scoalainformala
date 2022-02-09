# print("Mesaj")
# format()
# a = input("Input dat de utilizator")
# def functia_mea(param_1):
#     pass

def suma(a: int, b: int, c: int = 0) -> (int, int):
    """
    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum of params
    """
    return a + b + c, a - b - c

variabila_1 = 1
variabila_2 = 2
sum, dif = suma(a=variabila_1, c=0, b=variabila_2)
print(sum, dif)