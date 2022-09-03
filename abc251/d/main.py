W = int(input())

l = []
for i in range(99):
    l.append(i + 1)
    l.append((i + 1) * 100)
    l.append((i + 1) * 10000)

print(297)
print(*l)