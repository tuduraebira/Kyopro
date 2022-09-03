from decimal import Decimal


a, b, c = map(int, input().split())

if Decimal(str(a)) ** Decimal('0.5') + Decimal(str(b)) ** Decimal('0.5') < Decimal(str(c)) ** Decimal('0.5'):
    print("Yes")
else:
    print("No")