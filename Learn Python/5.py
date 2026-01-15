# OPERATOR

# 1\ Operator Aritmatika
a = 10
b = 3
print(a+b)
print(a - b)
print(a * b)
print(a / b)

print(a // b)   # bilangan bulat (hasil tanpa desimal)
print(a % b)    # Modulo (sisa pembagian)
# praktis Modulo
print(10 % 2)
print(11 % 2)

a = 2
b = 3
print(a ** b)
print(5 ** 2)

# 2\ Operator Assignment
x = 10
print("x awal:", x) #example
print(x)

x += 5
print("x setelah +=5:", x) # 15
print (x)

x -= 3
print(x)

x /= 5
print(x)

x *= 2
print(x)

# 3\ Operator Perbandingan
print(a > b)    # lebih besar: True
print(a < b)    # lebih kecil: False
print(a >= b)   # lebih besar atau sama: True
print(a <= b)   # lebih kecil atau sama: False
print(a == b)   # sama dengan: False
print(a != b)   # tidak sama denga: True

code1 = "coding"
code2 = "vibeCoding"
code3 = "Fusnuk"

print(code1 == code3)
print(code3 != code2)

# 4\ Operator Logic
pekerja = 19000000
print(pekerja > 19000000 and pekerja < 100000)

umur = 25
print(umur > 25 and umur < 30)

hari = "sabtu"
print(hari == "sabtu" or hari == "minggu")

aktif = True
print(not aktif)

# 5\ Operator String
# Concatenation(+)
pekerja = "19jt pekerja"
loker = "Deforestasi Sawit"
info = pekerja + "" + loker
print(info)

# Repetition(*)
lahan = "-"
print(lahan*30)

# Membership(in)
info = "Program Deforestasi Sawit akan di laksanakan pada daerah bencana Sumatra"
print("Deforestasi" in info)
print("19juta pekerja" in info) #false
print("Sawit" in info)

# 6\ Precedance Operator
# Pangkat (**)

# Perkalian dan Pembagian (*,/,//,%)
# Penjumlahan dan Pengurangan (+,-)
# Perbandingan (==, !=, >, <, <=, >=)
# Logic not
# Logic and
# Logic or