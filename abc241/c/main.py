def calc(x, y, dx, dy):
    count = 0
    for i in range(6):
        if not (0 <= min(x, y) and max(x, y) < N):
            return False
        if S[x][y] == '#':
            count += 1
        x += dx
        y += dy
    return count >= 4

N = int(input())
S = [input() for _ in range(N)]

Dx = [1, 0, 1, 1]
Dy = [0, 1, 1, -1]
for x in range(N):
    for y in range(N):
        for dx, dy in zip(Dx, Dy):
            if calc(x, y, dx, dy):
                print("Yes")
                exit()
print("No")