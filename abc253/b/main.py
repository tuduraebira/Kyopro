H, W = map(int, input().split())
S = [input() for _ in range(H)]

pos = []
for i, s in enumerate(S):
    for j, c in enumerate(s):
        if c == 'o':
            pos.append([i, j])

print(abs(pos[0][0] - pos[1][0]) + abs(pos[0][1] - pos[1][1]))