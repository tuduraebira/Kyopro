N, K, A = map(int, input().split())
pt = A

for _ in range(K - 1):
    pt += 1
    if pt > N:
        pt = 1

print(pt)