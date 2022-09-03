n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_cnt = {}
b_cnt = {}

hit = 0
blow = 0

for i in range(n):
    if a[i] == b[i]:
        hit += 1

for i in range(n):
    for j in range(n):
        if a[i] == b[j] and i != j:
            blow += 1

print(hit)
print(blow)