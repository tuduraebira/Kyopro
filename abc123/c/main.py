N = int(input())
time = [int(input()) for _ in range(5)]

mi = min(time)

print(int(4 + (N + mi - 1) / mi))