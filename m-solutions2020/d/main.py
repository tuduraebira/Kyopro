N = int(input())
A = list(map(int, input().split()))

isdown = False
first_isdown = False
pr = []
for i in range(len(A) - 1, 0, -1):
    if A[i] > A[i - 1]:
        first_isdown = True

    if first_isdown and isdown and A[i] < A[i - 1]:
        isdown = False
        pr.append(2)
    elif first_isdown and not isdown and A[i] > A[i - 1]:
        isdown = True
        pr.append(1)
    else:
        pr.append(0)
if isdown:
    pr.append(2)
else:
    pr.append(0)

#print(pr)

ans = 1000
kabu = 0
for i, p in enumerate(pr[::-1]):
    if p == 2:
        kabu = ans // A[i]
        ans %= A[i]
    elif p == 1:
        ans += kabu * A[i]
        kabu = 0
    #print(ans, kabu)

print(ans)
