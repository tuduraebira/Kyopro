N = int(input())
C = list(map(int, input().split()))

dp = [[0] * N for _ in range(9)]

for i in range(9):
    for j in range(N):
        