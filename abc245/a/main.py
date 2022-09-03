import datetime


A, B, C, D = map(int, input().split())

if datetime.time(A, B, 0) < datetime.time(C, D, 1):
    print("Takahashi")
else:
    print("Aoki")