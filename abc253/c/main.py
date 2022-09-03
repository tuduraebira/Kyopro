Q = int(input())

s = set()
cnt = {}
for _ in range(Q):
    q, *num = map(str, input().split())
    if q == '1':
        s.add(int(num[0]))
        if cnt.get(num[0]) != None:
            cnt[num[0]] += 1
        else:
            cnt[num[0]] = 1
    elif q == '2':
        if cnt.get(num[0]) != None:
            cnt[num[0]] -= min(cnt[num[0]], int(num[1]))
            if cnt[num[0]] == 0:
                s.remove(int(num[0]))
    else:
        l = list(s)
        print(l)
        print(l[-1] - l[0])
        