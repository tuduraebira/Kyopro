H, W = map(int, input().split())
G = [input() for _ in range(H)]
isVisit = [[False] * W for _ in range(H)]


i, j = 0, 0
while True:
    isVisit[i][j] = True

    if G[i][j] == 'U':
        if i - 1 < 0:
            print(i+1, j+1)
            exit()
        else:
            i -= 1
    elif G[i][j] == 'D':
        if i + 1 >= H:
            print(i+1, j+1)
            exit()
        else:
            i += 1
    elif G[i][j] == 'L':
        if j - 1 < 0:
            print(i+1, j+1)
            exit()
        else:
            j -= 1
    elif G[i][j] == 'R':
        if j + 1 >= W:
            print(i+1, j+1)
            exit()
        else:
            j += 1

    if isVisit[i][j]:
        print(-1)
        exit()