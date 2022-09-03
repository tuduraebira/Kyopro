A, B = map(str, input().split())

for i in range(min(len(A), len(B))):
    if int(A[-1 - i]) + int(B[-1 - i]) >= 10:
        print("Hard")
        exit()

print("Easy")