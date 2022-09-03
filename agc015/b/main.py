S = input()
up_wa = [0]
down_wa = [0]
up = 0
down = 0
for s in S:
    if s == 'U':
        up += 1
    else:
        down += 1
    up_wa.append(up)
    down_wa.append(down)

ans = 0
for i, s in enumerate(S):
    ans += len(S) - 1
    if s == 'U':
        ans += i
    else:
        ans += len(S) - i - 1

print(ans)