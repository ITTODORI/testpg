# Fixed Error
# 1\ Try-Except
print("=== DATA CORRUPTION GOVT ===")

try:
    buget = int(input("Buget: "))
    expend = int(input("Expend: "))
    hasil = buget / expend
    print("Corrupt:", hasil)
except:
    print("Terjadi error dalam perhitungan bahlil!")
print("=== MENUJU GENERASI CEMAS ===")

# 2\ Specifik Error
try:
    x = int(input("Horizontal: "))
    y = int(input("Vertical: "))
    size = x / y
    print("Size ration:", size)
except ValueError:
    print("Masukan value")
except ZeroDivisionError:
    print("Ratio tidak cocok!")
except:
    print("Terjadi Error")

# 3\ Try-Execpt-Else
try:
    value = int(input("Value:"))
except ValueError:
    print("Numb only")
else:
    print("your value", value)
    if value > 0:
        print("stats", "Positive")
    elif value < 0:
        print("stats", "Negaitve")
    else:
        print("Null")