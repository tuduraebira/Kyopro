n = int(input())
R = list(map(int, input().split()))
C = list(map(int, input().split()))
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]

tmp = []
for r, c in query:
    tmp.append([R[r - 1], C[c - 1]])

ans = ''
for r, c in tmp:
    if r + c >= n + 1:
        ans += '#'
    else:
        ans += '.'

print(ans)