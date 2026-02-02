# PACKAGE
import package.pack
from package import physics
from package.physics import force as gaya

result_x = package.pack.multiplication(1,2,3,4,5)
print(f"Saldo x : {result_x}")

force = physics.force(90,10)
print(f"Force > {force}")

force = gaya(90,20)
print(f"Force > {force}")