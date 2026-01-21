# LOOPING
# 1\ for Loop
for i in range(5):
    print("Hedoeepp Jo Ko Wee !!")
    print(i)

for i in range(1,6):
    print("Deforestasi Sawit", 1)

for i in range(10, 0, -1):
    print(i, "Ijazahmu Palsu!")

# 2\ for Loop by Str
framework = "JokoUI"
for huruf in framework:
    print(framework)

Database = input("Platform")
for huruf in Database:
    print("-", Database)

# 3\ While Loop
hutang = 1
while hutang <= 5:
    print(hutang)
    hutang += 1         #fungsi penghentian loop

jawaban = ""
while jawaban != "Bahlil":
    jawaban = input("Siapa mentri ESDM? ")
    if jawaban != "Bahlil":
        print("pelakunya \'Bahlil\' Tololll....!")
print("Lu yang milih, bukan gw!")

# 4\ Break and Continues
ijazah_rahasia = 8

while True:
    jawaban = int(input("Presiden Prabowo berada di nomor berapa? "))

    if jawaban == ijazah_rahasia:
        print("1, 2, 3. OKE GAS!")
        break
    else:
        print("tahun 2025")

ijazah_rahasia = "Mulyono"

while True:
    jawaban = input("Dokumen rahasia nama Presiden ke-7? ")
    
    if jawaban == ijazah_rahasia:
        print("Waghh..! KAGET")
        break
    else:
        print("whoo.. yaa ndak tau kok tanya-tanya saya")

# 5\ Continue
for i in range(10):
    if i % 2 == 0=
        if i % 2 == 0:      # jika ganjil
            continue        # lewati, lanjut angka berikutnya
        print(i, "Ganjil")  # hanya mencetak ganjil

# 6\ for Else
# character letters
char = input("DOKSIL : ")
search = input("Searching : ")

for key in char:
    if key == search:
        print("key :", search, "| it's DOKSIL!")
        break
else:
    print("key :", search, "| Data bersifat Private Govt!")

# Keyword
keyword = input("DOKSIL : ")
search = input("Searching : ")

if search in keyword:
        print("Word >", "\'",search,"\'", "DOKSIL")
else:
    print("Word >", "\'",search,"\'", "Data bersifat Private Govt!")
