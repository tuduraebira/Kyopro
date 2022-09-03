N = int(input())
A = list(map(int, input().split()))
Aa = [0] + A + [0]
As = []
for i in range(N + 1):
    As.append(abs(Aa[i] - Aa[i + 1]))
s = sum(As)

for i in range(N):
    s2 = s - (As[i] + As[i + 1])
    s2 += abs(Aa[i] - Aa[i + 2])
    print(s2)