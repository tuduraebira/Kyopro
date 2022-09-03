N = int(input())
s = input()

ans = N
res = []
for c in s:
    res.append(c)
    if res[-3:] == ["f", "o", "x"]:
        for _ in range(3):
            res.pop()
        ans -= 3

print(ans)