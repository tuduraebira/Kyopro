R, C = map(int, input().split())
A = []
for _ in range(2):
    A1, A2 = map(int, input().split())
    A.append([A1, A2])

print(A[R - 1][C - 1])