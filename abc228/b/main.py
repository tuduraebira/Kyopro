N, X = map(int, input().split())
A = list(map(int, input().split()))
isSpeak = [0] * N
isSpeak[X - 1] = 1
pt = X - 1

while True:
    if isSpeak[A[pt] - 1] == 1:
        print(sum(isSpeak))
        break
    else:
        isSpeak[A[pt] - 1] = 1

    pt = A[pt] - 1