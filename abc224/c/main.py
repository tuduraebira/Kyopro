import itertools


N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for v in itertools.combinations(XY, 3):
    v_s = sorted(v)
    if v_s[0][0] == v_s[1][0] and v_s[1][0] == v_s[2][0]:
        continue
    elif v_s[0][0] == v_s[1][0] or v_s[1][0] == v_s[2][0]:
        ans += 1
    else:
        if (v_s[1][1] - v_s[0][1]) / (v_s[1][0] - v_s[0][0]) == (v_s[2][1] - v_s[1][1]) / (v_s[2][0] - v_s[1][0]):
            continue
        ans += 1

print(ans)