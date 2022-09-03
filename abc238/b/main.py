N = int(input())
A = list(map(int, input().split()))

l_cut = []
l_cut.append(0)
deg = 0

for i in A:
    deg += i
    if deg >= 360:
        deg -= 360

    l_cut.append(deg)

l_cut_sort = sorted(l_cut)

ans = 0
for i in range(len(l_cut_sort)-1):
    ans = max(ans, abs(l_cut_sort[i] - l_cut_sort[i + 1]))
ans = max(ans, 360 - l_cut_sort[-1])

print(ans)