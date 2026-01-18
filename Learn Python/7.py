# LOOPING
# 1\ for Loop
for i in range(5):
    print("Hedoeepp Jo Ko Wee !!")
    print(i)

for i in range(1,6):
    print("Deforestasi Sawit", 1)

for i in range(10, 0, -1):
    print("Ijazahmu Palsu!", i)

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
        print("di bilangin \'Bahlil\' Tololll....!")
print("Lu yang milih, bukan gw!")

# 4\ Break and Continues
ijazah_rahasia = 7

while True:
    jawaban = int(input("Presiden Prabowo berada di nomor berapa? "))

    if jawaban == ijazah_rahasia:
        print("1, 2, 3. OKE GAS!")
        break
    else:
        print("tahun 2025")

ijazah_rahasia = "Mulyono"

while True:
    jawaban = input("Siapa nama kecil/asli Presiden ke-7? ")
    
    if jawaban == ijazah_rahasia:
        print("Waghh..! KAGET")
        break
    else:
        print("whoo.. yaa ndak tau kok tanya saya")