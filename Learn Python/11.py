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