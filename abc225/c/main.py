N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i + 1 != N:
            if B[i + 1][j] - B[i][j] != 7:
                print("No")
                exit()

        if j + 1 != M:
            if B[i][j + 1] - B[i][j] != 1:
                print("No")
                exit()
            
            if B[i][j] % 7 == 0 and B[i][j + 1]:
                print("No")
                exit()

        if j - 1 >= 0:
            if B[i][j] % 7 == 1 and B[i][j - 1]:
                print("No")
                exit()
print("Yes")