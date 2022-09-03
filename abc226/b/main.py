N = int(input())
cnt = {}

for _ in range(N):
    L, *a = map(int, input().split())
    a = tuple(a)
    if cnt.get(a) == None:
        cnt[a] = True

print(len(cnt))