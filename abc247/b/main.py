from collections import defaultdict


N = int(input())
name = [list(map(str, input().split())) for _ in range(N)]

st = defaultdict(int)
for s, t in name:
    st[s] += 1
    st[t] += 1
#print(st)

for s, t in name:
    if s == t:
        if st[s] != 2 and st[t] != 2:
            print("No")
            exit()
    elif st[s] != 1 and st[t] != 1:
        print("No")
        exit()

print("Yes")