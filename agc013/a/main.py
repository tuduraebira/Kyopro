N = int(input())
A = list(map(int, input().split()))

switch = []
d = ''
for i in range(N - 1):
    if A[i] == A[i + 1]:
        switch.append(False)
    elif A[i] > A[i + 1]:
        if d == 'u':
            switch.append(True)
            d = ''
        else:
            switch.append(False)
            d = 'd'
    else:
        if d == 'd':
            switch.append(True)
            d = ''
        else:
            switch.append(False)
            d = 'u'

#print(switch)
print(sum(switch) + 1)