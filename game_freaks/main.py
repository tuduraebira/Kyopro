from queue import Queue

# 入力
step = int(input())
H, W = map(int, input().split())
c = [input() for _ in range(H)]

# 四方向の移動量
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# 戦ったトレーナーを格納する集合
se = [[set()] * W for _ in range(H)]
# スタートからの距離
dist = [[-1] * W for _ in range(H)]


# A, B, トレーナーの位置を探索
for i, s in enumerate(c):
    for j, char in enumerate(s):
        if char == 'A':
            sx, sy = i, j
        elif char == 'B':
            gx, gy = i, j


# どこのトレーナーと戦うか探索
battle = [[(-1, -1)] * W for _ in range(H)]
for i, s in enumerate(c):
    for j, char in enumerate(s):
        if char == 'N':
            for k in range(i - 1, -1, -1):
                if c[k][j] != '.':
                    break
                battle[k][j] = (i, j)
        elif char == 'S':
            for k in range(i + 1, H):
                if c[k][j] != '.':
                    break
                battle[k][j] = (i, j)
        elif char == 'W':
            for k in range(j - 1, -1, -1):
                if c[i][k] != '.':
                    break
                battle[i][k] = (i, j)
        elif char == 'E':
            for k in range(j + 1, W):
                if c[i][k] != '.':
                    break
                battle[i][k] = (i, j)


# BFS
que = Queue()
dist[sx][sy] = 0
que.put((sx, sy))
while not que.empty():
    x, y = que.get()

    for dx, dy in zip(dxs, dys):
        x2, y2 = x + dx, y + dy

        # マップ外，障害物，トレーナーがいるところは調べない
        if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W or c[x2][y2] == '#' or c[x2][y2] in ['N', 'S', 'E', 'W']:
            continue
        
        # 一度更新したところは，最短歩数が同じかつ戦うトレーナーの数が多くなる場合のみ更新
        if dist[x2][y2] != -1:
            if dist[x2][y2] == dist[x][y] + 1:
                if len(se[x][y]) > len(se[x2][y2]):
                    se[x2][y2] = set(se[x][y])
                elif len(se[x][y]) == len(se[x2][y2]) and battle[x2][y2] != (-1, -1):
                    se[x][y].add(battle[x][y])
                    se[x2][y2].add(battle[x][y])
                    if len(se[x][y]) > len(se[x2][y2]):
                        se[x2][y2] = set(se[x][y])
            continue
        
        # 距離と戦ったトレーナーを更新
        dist[x2][y2] = dist[x][y] + 1
        se[x2][y2] = set(se[x][y])
        if battle[x2][y2] != (-1, -1):
            se[x2][y2].add(battle[x2][y2])

        que.put((x2, y2))


# 出力
print(dist[gx][gy], len(se[gx][gy]))