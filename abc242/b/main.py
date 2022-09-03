S = input()

S_min = sorted(S)

ans = ""
for s in S_min:
    ans += s
print(ans)