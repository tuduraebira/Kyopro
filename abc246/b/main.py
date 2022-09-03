from math import sqrt


A, B = map(int, input().split())

naname_len = sqrt(A * A + B * B)

print(A / naname_len, B / naname_len)