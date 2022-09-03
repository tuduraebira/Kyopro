N = int(input())

A = 1
num = [1, 1]
for i in range(N):
    if i == 0:
        print(A)
        continue
    
    num_tmp = []
    for j in range(i - 1):
        n = num[j] + num[j + 1]
        num_tmp.append(n)

    num = [1] + num_tmp + [1]
    print(*num)