from collections import deque


Sa = input()
Sb = input()
Sc = input()

deqA = deque(Sa)
deqB = deque(Sb)
deqC = deque(Sc)
deqA.append('a')
deqB.append('b')
deqC.append('c')

nx = 'a'
while len(deqA) > 0 and len(deqB) > 0 and len(deqC) > 0:
    if nx == 'a':
        nx = deqA.popleft()
    elif nx == 'b':
        nx = deqB.popleft()
    else:
        nx = deqC.popleft()

if nx == 'a':
    print('A')
elif nx == 'b':
    print('B')
else:
    print('C')