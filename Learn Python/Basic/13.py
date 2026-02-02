# MODULES
# 1\ Main
import fileIMPORT

result_sum = fileIMPORT.summation(1,2,3,4,5)
print(f"Saldo Sum : {result_sum}")

result_x = fileIMPORT.multiplication(1,2,3,4,5)
print(f"Saldo x : {result_x}")

exp_3 = fileIMPORT.exponents(3)
print(f"Saldo exp3 : {exp_3(3)}")

# 2\ Main From (Recom)
from fileIMPORT import summation

result_sum = summation(1, 2, 3, 4, 5)
print(f"Saldo Sum : {result_sum}")

from fileIMPORT import multiplication,exponents #Grubing import

result_sum = multiplication(1, 2, 3, 4, 5)
print(f"Saldo Sum : {result_sum}")

exp_3 = exponents(3)
print(f"Saldo exp3 : {exp_3(3)}")

# 3\ from ALIAS
import fileIMPORT as math
result_sum = math.summation(1,2,3,4,5)
print(f"Saldo Sum : {result_sum}")

from fileIMPORT import multiplication as x

result_x = x(1, 2, 3, 4, 5)
print(f"Saldo X : {result_sum}")