# Manipulation Str
# false code
nama = "iMen"
berat = 60

pesan = "Nama saya" + nama + ",berat" + berat
print(pesan)

# True code
pesan = "Nama saya" + nama + ",berat" + str(berat)

# Panjang Str
panjang_nama = len(nama)
panjang_pesan = len(pesan)

print(panjang_nama)
print(panjang_pesan)
print(len(nama))
print(len(pesan))

# Indexing Str
nama = "Python"
print(nama[0]) # huruf pertama
print(nama[1]) # huruf kedua
print(nama[2]) # huruf ketiga

print(nama[-1]) # huruf terakhir
print(nama[-2]) # huruf kedua dari akhir
print(nama[-3]) # huruf ketiga dari akhir

# Slicing Str
nama = "Python"
print(nama[0:3]) # Pyt (index 0,1,2)
print(nama[2:5]) # tho (index 2,3,4)
print(nama[1:4]) # yth (index 1,2,4)

nama = "Python"
print(nama[:3]) # Pyt (dari awal hingga index 2)
print(nama[2:]) # tho (dari 2 hingga akhir)
print(nama[]) # Python (seluruh str)

# Methods Str
# Upper
nama = "Imen"
nama_upper = nama.upper()
print(nama_upper)

# Lower
nama_lower = nama.lower()
print(nama_lower)

# Tittle
nama = "Imen Code"
nama_title = nama.title()
print(nama.title())

# Capitalize
nama_capitalize = nama.capitalize()
print(nama.capitalize())

# Strip
nama = "  iMen  "
nama_strip = nama.strip()
print(nama_strip)

# Replace
kalimat = "Programer Handal Enggan Ngoding"
kalimat_baru = kalimat.replace("Handal", "Scroll Fusnuk")
print(kalimat_baru)

# Count
kalimat = "Programer Handal Enggan Ngoding"
jumlah_a = jumlah.count("a")
print(jumlah.a)

# Find
kalimat = "Programer Handal Enggan Ngoding"
posisi = kalimat.find("Ngoding")
print(posisi)

# Escape Characters
kalimat = "mana info\nloker 19jt"
print(kalimat)
# Tabs
kalimat = "nama\t= iMen\nberat\t= 170cm"
print(kalimat)
# Backslash
lokasi = "C:\\iMen\\coding" # Error code [lokasi = "C:\iMen\coding]"
# String
pesan = "Pada gila Wanita gue gila \'Coding\'"
print(pesan)

# Interpolation
# F-String
pekerja = 19000000
pohon = "Sawit"
lokasi = "Sumatra"

notice = "kita akan kerahkan {pekerja} pekerja untuk menanam pohon {pohon} di daerah {lokasi} sana.\n {pohon} juga pohon kan, berdaun."
print(notice)
# F-String by Expressions
sawit = 76000
lahan = 250

total = f"Total : Rp {sawit * lahan:,}"
print (total)

pekerja = 19000000
pohon = "Sawit"
lokasi = "Sumatra"

pekerja_19jt = f"{pekerja:,}".replace(",", ".")

notice = f"kita akan kerahkan {pekerja_19jt} pekerja untuk menanam pohon {pohon} di daerah {lokasi} sana.\n Kelapa {pohon} itu pohon, ada daunnya."
print(notice)

nama = "Jokowi"

notice = f"hidup{nama.upper()}"