N = int(input())
A = list(map(int, input().split()))
isTrue = [False] * 2001

for a in A:
    isTrue[a] = True

for i in range(2001):
    if isTrue[i] == False:
        print(i)
        exit()