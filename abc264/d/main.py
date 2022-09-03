S = input()

cs = 'atcoder'
ans = 0
for i in range(len(S)):
    if S[i] == cs[i]:
        continue

    index = cs.find(S[i])
    ans += index - i
    cs = S[i] + cs[:index] + cs[index+1:]

print(ans)