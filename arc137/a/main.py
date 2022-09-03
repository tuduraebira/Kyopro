from math import gcd


L, R = map(int, input().split())

if R % 2 == 0:
    ans = R - ((R // 2) + 1)
else:
    ans = R - (R // 2)
    
for i in range(L, R // 2):
    if gcd(i, R) == 1:
        ans = max(ans, R - i)

print(ans)