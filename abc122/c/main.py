from bisect import bisect_left


N, Q = map(int, input().split())
S = input()
Apt = []
for i, s in enumerate(S):
    if s == 'A':
        if i + 1 != N and S[i + 1] == 'C':
            Apt.append(i + 1)

for _ in range(Q):
    l, r = map(int, input().split())

    ll = bisect_left(Apt, l)
    rr = bisect_left(Apt, r)

    print(rr - ll)