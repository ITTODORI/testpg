# Type Basic
# +Integer (int) - Bilangan Bulat

umur = 20
saldo = -19000000
nol = 0

print(type(umur)) #<class 'int'>

# +Float - Bilangan Desimal

tinggi = 170.5
suhu = -10.5

# Notasi scientific
speed_of_light = 3e8    # 3 x 10^8 = 300000000
very_small = 1e-6       # 0.000001

# +String (str) - Text

nama = 'iMen'
kota = 'Earthtown'
# string multi-line
pesan = """
Samlekom mamank JAWIR
yang sangat
IIIIIRRREENGG disana
"""

# +Boolean (bool) - True/False
is_student = True
is_married = False
has_license = True

print(type(is_student))

# Assignment Basic
nama = "iMen"
is_active =  True

# Multiple Assigment
x = y = z = 0 # semua variabel 0
a, b, c = 1, 2, 3 # a=1 b=2 c=3
name, age = "iMen", 25 # name="iMen", age=25

# Mengubah nilai Variabel
skor = 90
print(skor) # 90 
                    # mengubah nilai (program berjalan dari atas-bawah)
skor = 100
print(skor) # 100

# Menggunakan Variabel
panjang = 10
lebar = 5
luas = panjang * lebar

print("luas : ")
print(luas)

panjang = 10
lebar = 5
luas = panjang * lebar

print("luas : ", luas)