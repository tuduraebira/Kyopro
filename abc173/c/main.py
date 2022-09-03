H, W, K = map(int, input().split())
c = [input() for _ in range(H)]
rsum = [0] * H
csum = [0] * W
all_sum = 0
for i in range(H):
    for j in range(W):
        if c[i][j] == '#':
            rsum[i] += 1
            csum[j] += 1
            all_sum += 1

# print(rsum)
# print(csum)
ans = 0
for i in range(1 << H):
    for j in range(1 << W):
        red_sum = 0
        row = []
        col = []
        for k in range(H):
            if (i >> k) & 1:
                red_sum += rsum[k]
                row.append(k)
        for l in range(W):
            if (j >> l) & 1:
                red_sum += csum[l]
                col.append(l)
        for ro in row:
            for co in col:
                if c[ro][co] == '#':
                    red_sum -= 1

        if all_sum - red_sum == K:
            ans += 1

print(ans)