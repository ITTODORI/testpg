# STRUCTURE CONTROL

# 1\ If
angka = int(input("masukan angka: "))
if angka > 0:
    print("angka positif")
if angka < 0:
    print("angka negatif")

if angka == 0:
    print("angka nol")

# 2\ If-Else
nilai = int(input("masukan nilai: "))
if nilai >= 60:
    print("Anda Lulus")
else:
    print("Anda tidak Lulus")

# 3\ Elif (Else - If)
pekerja = int(input("Info loker: "))
if pekerja >= 20:
    print("PT JokoUI")
elif pekerja >= 50:
    print("PT gibRun")
elif pekerja >= 70:
    print("PT SawitDB")
elif pekerja >= 80:
    print("PT PraboGO")
else:
    print("HIDUP JOKOWI !")

# 4\ Operator Logic
umur = int(input("Masukan umur: "))
ijazah = input("Punya Ijazah? (ya/tidak): ")

if umur >= 17 and ijazah == "asli":
    print("Boleh bekerja")
else:
    print("Ijazahmu palsu ngn***")

# 5\ Nested if
username = input("Username: ")
password = input("Password: ")

if username == "loker":
    if password == "19juta":
        print("Login berhasil")
        print("Selamat, Berjuang, dan Sukses Selalu (mencariLOKER)")
    else:
        print("Mana 19jt loker yang kau janjikan itu?!")
else:
    print("Indonesia CEMAS KAU DEK !!")

# 6\ Match Case
gaji = input("Masuk kerja: ").lower()

match gaji:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat" :
        print("Hari Gajian")
    case "sabtu" | "ahad" :
        print("Gaji Lembur")
    case _:
        print("Hari tidak Kerja")

# 7\ Conditional Expression (Ternary Operator)
pajak = int(input("Masukan Nominal: "))
hasil = "Lunas" if pajak > 0 else "Hutang"
print(hasil)
    #Code jadi ringkas dan simple dari materi 2\ If-Else