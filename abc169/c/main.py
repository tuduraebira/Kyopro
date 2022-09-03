from decimal import Decimal
from math import floor


A, B = input().split()
A = Decimal(A)
B = Decimal(B)

print(floor(A * B))