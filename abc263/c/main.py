import sys
sys.setrecursionlimit(10 ** 8)


def rec(l, num, cnt):
    tmp = l
    for i in range(num, M + 1):
        if tmp[-1] < i:
            cnt += 1

            if len(tmp) == N:
                print(*tmp[1:], i)
                continue
            else:
                tmp.append(i)
                rec(tmp, i + 1, cnt)
                tmp.pop()


N, M = map(int, input().split())
ans = [0]
rec(ans, 1, 0)
