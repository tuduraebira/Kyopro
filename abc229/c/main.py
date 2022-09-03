N, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(reverse=True)

ans = 0
weight = 0
pt = 0

while pt < len(AB):
    num = 0
    weight += AB[pt][1]

    if weight > W:
        num = AB[pt][1] - (weight - W)
        ans += AB[pt][0] * num
        break
    else:
        num = AB[pt][1]
        ans += AB[pt][0] * num

    pt += 1

print(ans)