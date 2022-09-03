N = int(input())
cnt = {}
for _ in range(N):
    name = input()
    if cnt.get(name):
        cnt[name] += 1
    else:
        cnt[name] = 1

cnt_sort = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
print(cnt_sort[0][0])