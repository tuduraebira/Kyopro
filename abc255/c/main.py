X, A, D, N = map(int, input().split())

if D == 0:
    print(abs(X - A))
    exit()

index = (X - A) / D
if index <= 0:
    print(abs(X - A))
elif index >= N - 1:
    print(abs(X - (D * (N - 1) + A)))
else:
    print(min(abs(X - (D * (int(index)) + A)), abs(X - (D * (int(index) + 1) + A))))