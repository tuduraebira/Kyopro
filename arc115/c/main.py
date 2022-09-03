N = int(input())

li = [1] * (N + 1)

for i in range(2, N + 1):
    li[i] += 1
    tmp = i
    while tmp <= N:
        li[tmp] = max(li[i], li[tmp])
        tmp += i

print(*li[1:])