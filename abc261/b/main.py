N = int(input())
A = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        if A[i][j] == 'W' and A[j][i] == 'L' or A[i][j] == 'L' and A[j][i] == 'W' or A[i][j] == 'D' and A[j][i] == 'D':
            continue
        else:
            print('incorrect')
            exit()

print('correct')