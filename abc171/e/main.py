N = int(input())
a = list(map(int, input().split()))

all_xor = a[0]
for i in range(1, N):
    all_xor ^= a[i]

ans = []
for n in a:
    tmp = all_xor
    ans.append(tmp ^ n)

print(*ans)