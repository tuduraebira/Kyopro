N = int(input())
T = input()

point = [0, 0]
muki = [[0, 1], [1, 0], [0, -1], [-1, 0]]
m = 1

for t in T:
    if t == 'S':
        point[0] += muki[m][0]
        point[1] += muki[m][1]
    elif t == 'R':
        m += 1
        m %= 4

print(*point)