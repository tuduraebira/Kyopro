A, B, X = map(int, input().split())

left = 0
right = 10 ** 18 + 10
while right - left > 1:
    mid = (left + right) // 2
    if A * mid + B * len(str(mid)) <= X:
        left = mid
    else:
        right = mid
    #print(left, right)

if left > 10 ** 9:
    left = 10 ** 9

print(left)