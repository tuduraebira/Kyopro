N, X = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 10 ** 40
min_num = 10 ** 10
ab = 0
for i in range(len(AB)):
    min_num = min(min_num, AB[i][1])
    ab += sum(AB[i])
    ans = min(ans, ab + min_num * (X - (i + 1)))

print(ans)