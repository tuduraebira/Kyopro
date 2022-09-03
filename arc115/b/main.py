N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

tate = []
yoko = []
for i in range(N):
    t = []
    y = []
    for j in range(N - 1):
        t.append(C[j][i] - C[j + 1][i])
        y.append(C[i][j] - C[i][j + 1])
    
    tate.append(t)
    yoko.append(y)

#print(tate, yoko)
for i in range(N - 1):
    if tate[i] != tate[i + 1] or yoko[i] != yoko[i + 1]:
        print("No")
        exit()

print("Yes")
index = -1
num = 10 ** 18
for i in range(N):
    if num > C[i][0]:
        index = i
        num = C[i][0]

A = []
B = C[index]
for i in range(N):
    if index == i:
        A.append(0)
    else:
        A.append(abs(C[i][0] - C[index][0]))

print(*A)
print(*B)