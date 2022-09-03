N, A, B = map(int, input().split())

ans = [[''] * (B * N) for _ in range(A * N)]

for i in range(A * N):
    for j in range(B * N):
        if (i // A) % 2 == 0:
            if (j // B) % 2 == 0:
                ans[i][j] = '.'
            else:
                ans[i][j] = '#'
        else:
            if (j // B) % 2 == 0:
                ans[i][j] = '#'
            else:
                ans[i][j] = '.'

for l in ans:
    print(''.join(l))