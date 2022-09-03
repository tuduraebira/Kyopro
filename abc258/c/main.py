N, Q = map(int, input().split())
S = input()

q = 0
for _ in range(Q):
    ts, xs = map(str, input().split())
    t = int(ts)
    x = int(xs)

    if t == 1:
        q += x
    else:
        print(S[-(q % N) + (x - 1)])