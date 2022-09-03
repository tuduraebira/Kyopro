N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ap = 0
bp = 0
mi = 0
ans = 0
while True:
    if mi >= K:
        break

    if A[ap] <= B[bp]:
        mi += A[ap]
        ans += 1
        ap += 1
    else:
        mi += B[bp]
        ans += 1
        bp += 1

print(ans)