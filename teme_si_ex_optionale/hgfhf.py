# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# string = string.replace("Inquisitor", "Conquistador")
# string = string.replace("Varric", "King")
# string = string.replace("Skyhold's", "Palace")
# print(string)
#
# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# new_text = "Cnq"
# print(string[0:81] + new_text[5:14])

# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced"
#
# start = "Conquistador"
#
# def exe1():
#     start = string[5:14]
#     if start:
#         print("Conquistador")
#     else:
#         print("Nu")
#         # a = i[5:14]
#         # b = i[26:31]
#         # c = i[43:49]
# # print(exe1("Cnq","king","Palace"))
#
# print(string)

# string = ["Claudiu", "Claudiu", "Claudiu"]
# substring = "Claudiu"
#
#
# count = string.count(substring)
#
#
# print(count)

# string = ['Maria', 'Irina', Claudiu, Ionut, Irina, Matei, ‘Irina’, ‘Maria’]

def nameChanger(x, y, z):
    string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
    # 42 -> 49
    # string = "The Inquisitor must meet Varric on top of Palace's battlements to be introduced."
    # 25 -> 31
    # string = "The Inquisitor must meet King on top of Palace's battlements to be introduced."

    start = string[5:14]
    end = string[26:31]
    text = string[43:49]
    string2 = string.replace(start, x)
    string3 = string2.replace(end, y)
    string4 = string3.replace(text, z)
    #print(string4)
string_value = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
lista = [[5, 14, 'Conquistador'], [26, 31, 'King'], [43, 49, 'Palace']]
for i in sorted(lista, reverse=True):
    #print(i, string_value[i[0]-1:i[1]])
    string_value = string_value.replace(string_value[i[0]-1:i[1]], i[2])
    print(string_value, '>>>')

nameChanger("Conquistador", "King", "Palace")
# #
#
# # num_calls = 0
# #
# #
# # def execitiu(x):
# #     global num_calls
# #     num_calls = 3
# #     num_calls += 1
# #     return x * x
# #
# # print(execitiu(4))
#
# # x = 1
# #
# #
# # def f():
# #     return x
# #
# #
# # print(x)
# # print(f())
#
# # x = (1, 2, 3)
# #
# # x[1] = 4
# x = [1, 2, "hello", "world", ["another", "list"]]
# print(len(x[3]))


