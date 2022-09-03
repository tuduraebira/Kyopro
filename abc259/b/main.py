from math import cos, radians, sin


a, b, d = map(int, input().split())

x = cos(radians(d)) * a - sin(radians(d)) * b
y = sin(radians(d)) * a + cos(radians(d)) * b

print(x, y)