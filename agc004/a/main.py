A, B, C = map(int, input().split())

if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    print(0)
    exit()

max_n = max(max(A, B), C)
l = max_n // 2
r = max_n - l

if max_n == A:
    print(abs(B * C * l - B * C * r))
elif max_n == B:
    print(abs(A * C * l - A * C * r))
else:
    print(abs(B * A * l - B * A * r))