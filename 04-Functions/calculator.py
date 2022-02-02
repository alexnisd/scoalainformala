# 2 variabila
# 1 operator
# 1 rezultat

def suma(a: int, b:int) -> str:
    return f"{a} + {b}= {a + b}"


def diferenta(a, b) -> str:
    return f"{a} - {b}= {a - b}"


def inmultire(a: int, b:int) -> str:
    return f"{a} * {b}= {a * b}"
def impartire(a: int, b:int) -> float:
    if b == 0:
       while b == 0:
            b = int(input("Aloca o noua valoare pentru b: "))
    return f"{a} / {b}= {a / b}"


def operator():
    op = input("Alege operatorul: ")
    if op == ['*', '/', '+', '-']:
        while op not in ['*', '/', '+', '-']:
            op = input("Alege operatorul: ")
    return op



def calculator():
    nr1 = int(input("Primul numar: "))
    nr2 = int(input('Al doilea: '))
    op = operator()
    if op == '+':
        rezultat = suma(nr1, nr2)
    elif op == '-':
        rezultat = diferenta(nr1, nr2)
    elif op == '*':
        rezultat = inmultire(nr1, nr2)
    elif op == '/':
        rezultat = impartire(nr1, nr2)
    # return f"{nr1} {op} {nr2} = ", eval(f"{nr1} {op} {nr2}")


print(calculator())