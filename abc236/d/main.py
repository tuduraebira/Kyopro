import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
A = [list(map(int, input().split())) for _ in range(2 * N - 1)]

for i in range(2 * N - 1):
    A[i] = [-1] * (i + 1) + A[i]

def dfs(sets, value):
    ans = []
    if not sets:
        return value

    i = min(sets)
    sets ^= {i}
    for j in sets:
        ans.append(dfs(sets ^ {j}, value ^ A[i][j]))
    return max(ans)

sets = set(range(N * 2))

print(dfs(sets, 0))