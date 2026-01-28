# 8\ Type Error
print("Hello World"
    # > Syntax tidak di temukan
print(name)
    # > Variable 'name' belum di definisikan
print("name" + 5)
    # > Kesalahan type data, tidak bisa menambahkan str dengan angka TypeError: can only concatenate str (not "int") to str
angka=int("error")
    # > ValueError, nilai tidak valid tidak bisa convert "error" ke int
list_data = [1,2,3]
print(list_data[5])
    # > IndexError, index tidak valid/out of range
hero = {"Name" : "Mulyono"}
print(hero["Skill"])
    # > KeyError, key tidak valid
print(10 / 0)
    # > ZeroDivision, pembagian dengan 0

# Fixed Error
# 1\ Try-Except
print("=== KALKULATOR SEDERHANA ===")

try:
    angka1 = int(input("Angka pertama: "))
    angka2 = int(input("Angka kedua: "))
    hasil = angka1 / angka2
    print("Hasil:", hasil)
except:
    print("Terjadi error dalam perhitungan bahlil!")
print("===MENUJU GENERASI EMAS===")

# 2\ Specifik Error