N = int(input())
A = list(map(str, input().split()))
l = len(A)
s = ''
for a in A:
    s += a

n = int(s, 2)
#print(n)

if n == 0 or (2 ** (l - 2) <= n and n < 2 ** (l - 1)):
    print("Yes")
else:
    print("No")