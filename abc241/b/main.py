n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = {}
for i in a:
    if not cnt.get(i):
        cnt[i] = 1
    else:
        cnt[i] += 1

for i in b:
    if not cnt.get(i):
        print("No")
        exit()
    else:
        cnt[i] -= 1

for val in cnt.values():
    if val < 0:
        print("No")
        exit()

print("Yes")