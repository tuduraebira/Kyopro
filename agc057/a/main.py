T = int(input())

for _ in range(T):
    L, R = map(int, input().split())

    Rs = str(R)
    ma = -1
    for i in range(len(Rs)):
        for j in range(i + 1, len(Rs) + 1):
            if len(Rs[i:j]) != len(Rs):
                ma = max(ma, int(Rs[i:j]))

    if ma >= L:
        print(R - ma)
    else:
        print(R - L + 1)