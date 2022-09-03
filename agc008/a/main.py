x, y = map(int, input().split())

if x < y:
    print(min(y - x, abs(abs(y) - abs(x)) + 1))
elif y < x:
    if x * y > 0:
        print(abs(y - x) + 2)
    else:
        print(abs(abs(y) - abs(x)) + 1)
else:
    print(0)