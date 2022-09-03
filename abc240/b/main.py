N = int(input())
a = list(map(int, input().split()))
dif = {}

for i in a:
    dif[i] = True

print(len(dif))