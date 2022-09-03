n = int(input())
x, y = [], []
for _ in range(n):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)
s = input()

right_min, left_max = {}, {}

for i in range(n):
    if s[i] == 'R':
        if y[i] in left_max and x[i] < left_max[y[i]]:
            print("Yes")
            exit()
    else:
        if y[i] in right_min and right_min[y[i]] < x[i]:
            print("Yes")
            exit()

    if s[i] == 'R':
        if y[i] in right_min:
            right_min[y[i]] = min(x[i], right_min[y[i]])
        else:
            right_min[y[i]] = x[i]
    else:
        if y[i] in left_max:
            left_max[y[i]] = max(x[i], left_max[y[i]])
        else:
            left_max[y[i]] = x[i]

print("No")