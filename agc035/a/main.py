from collections import Counter


N = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)

if len(cnt) == 1:
    print("Yes" if cnt[0] == N else "No")
elif len(cnt) == 2:
    print("Yes" if cnt[0] == N // 3 else "No")
elif len(cnt) == 3:
    x, y, z = cnt.keys()
    print("Yes" if x ^ y ^ z == 0 and cnt[x] == cnt[y] == cnt[z] else "No")
else:
    print("No")