K = int(input())
K_2 = bin(K)[2:]

ans = ""
for n in K_2:
    if n == '1':
        ans += '2'
    else:
        ans += '0'

print(int(ans))