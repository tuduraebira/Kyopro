T = int(input())

for _ in range(T):
    N, A, B, X, Y, Z = map(int, input().split())

    x = 1 / X
    y = A / Y
    z = B / Z

    jun = []
    if x > y:
        jun.append(X)
        jun.append(Y)
    elif x < Y:
        jun.append(Y)
        jun.append(X)
    else:
        if X <= Y:
            jun.append(Y)
            jun.append(X)
        else:
            jun.append(X)
            jun.append(Y)

    if z > x:
        jun.insert(0, Z)
    elif z < x:
