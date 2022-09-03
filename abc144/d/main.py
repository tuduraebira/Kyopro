from math import atan, degrees


a, b, x = map(int, input().split())

half = a * a * b / 2

if x < half:
    print('{:.10}'.format(degrees(atan(a * b * b / (2 * x)))))
else:
    print('{:.10}'.format(degrees(atan((2 * b - 2 * x / (a * a)) / a))))