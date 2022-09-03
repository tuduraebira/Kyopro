from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(-1)
    exit()

amari = []
cnt = 0
res = 0
for i in range(N):
    if A[i] < B[i]:
        cnt += 1
        res += B[i] - A[i]
    elif A[i] > B[i]:
        amari.append(A[i] - B[i])

amari.sort(reverse=True)
wa = [0]
for i in range(len(amari)):
    wa.append(wa[i] + amari[i])

#print(amari, wa)

print(bisect_left(wa, res) + cnt)