# PACKAGE
import package.pack
from package import fisika
from package.fisika import gaya as gaya

result_x = package.pack.multiplication(1,2,3,4,5)
print(f"Saldo x : {result_x}")

gaya = fisika.gaya(90,10)
print(f"Gaya > {gaya}")

gaya = gaya(90,10)
print(f"Gaya > {gaya}")