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

# __init__.py
import package

result_sum = package.pack.summation(1,2,3,4,5)
print(f"Result + : {result_sum}")

force = package.physics.force(23,778)
print(f"Force > {force}")

# CUSTUMIZE INIT
from package import *

result_sum = package.pack.summation(1,2,3,4,5)
print(f"Result + : {result_sum}")

force = package.physics.force(23,778)
print(f"Force > {force}")