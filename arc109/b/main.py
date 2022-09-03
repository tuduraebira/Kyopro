N = int(input())

left = 0
right = N + 1
while abs(right - left) > 1:
    mid = abs(right + left) // 2
    if (mid * (mid + 1) // 2) <= N + 1:
        left = mid
    else:
        right = mid

print(N - left + 1)