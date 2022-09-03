S, T, X = map(int, input().split())

if T == 0:
    T = 24

if S < T:
    X += 0.5
    if S <= X and X <= T:
        print("Yes")
    else:
        print("No")
else:
    X += 0.5
    if S <= X or X <= T:
        print("Yes")
    else:
        print("No")