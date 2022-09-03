S = input()

num = [False] * 10
for s in S:
    num[int(s)] = True

for i, b in enumerate(num):
    if b == False:
        print(i)