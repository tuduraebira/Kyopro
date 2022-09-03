N, Q = map(int, input().split())
S = input()

for _ in range(Q):
    l, r = map(int, input().split())
    print(S.count("AC", l - 1, r))