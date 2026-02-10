# PACKAGE INDEX PYTHON [PIP]
    # pypi.org /Resources package index pthon
    # pip --version
    # pip list
    # python -m pip install --upgrade pip /install upgrade pip version
    # pip uninstall <pip> / delete, remove, uninstal

# NUMPY PACKAGE
import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list a = {list_a}")
#print(list_a**2) # error
print(f"vector a = {vector_a}")
print(f"a pangkat > {vector_a**2}")
print(f"a x 5 > {vector_a*5}")

matrix_b = np.array([(1,2),(3,4)])
print(f"Matrix :\n{matrix_b}")
print(f"Matrix ^2 :\n{matrix_b**2}")

zero_c = np.zeros((2,2))
print(f"Zero : \n{zero_c}")

ones_d = np.ones((2,2))
print(f"Ones : \n{ones_d}")

sum_bbd = matrix_b + matrix_b**2 + ones_d
print(f"Sum : \n{sum_bbd}")