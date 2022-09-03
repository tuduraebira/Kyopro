from bisect import bisect_left


X = int(input())

res = set()
for fir in range(1, 10):
    for d in range(-9, 9):
        s = ''
        dg = fir
        for i in range(19):
            s += str(dg)
            res.add(int(s))
            dg += d
            if 0 > dg or dg > 9:
                break
tosa = list(res)
tosa.sort()

print(tosa[bisect_left(tosa, X)])