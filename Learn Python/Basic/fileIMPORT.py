print("===| TESTER IMPORT |===")

hero = "Termulator"
stats = 9

def data(a:float, b:float)->float:
    return a/b

def summation(*args):
    saldo = 0
    for data in args:
        saldo += data
    return saldo

def multiplication(*args):
    saldo = 1
    for data in args:
        saldo *= data
    return saldo

def exponents(n:int):
    return lambda value:value**n