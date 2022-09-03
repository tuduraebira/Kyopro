N = int(input())

s = "1"
if N == 1:
    print(s)
    exit()

for i in range(1, N):
    s = s + " " + str(i + 1) + " " + s

print(s)