from bisect import bisect_left


N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

nijou = []
num = 0
while True:
    if num * num > N:
        break
    nijou.append(num * num)
    num += 1
nijou = nijou[1:]
#print(nijou)

ans = 0
for i in range(1, N + 1):
    soinsu = factorization(i)
    odd = 1
    for j in range(len(soinsu)):
        if soinsu[j][1] % 2 == 1:
            odd *= soinsu[j][0]

    left = -1
    right = len(nijou)
    while right - left > 1:
        mid = (right + left) // 2
        if odd * nijou[mid] <= N:
            left = mid
        else:
            right = mid
    ans += (left + 1)

print(ans)