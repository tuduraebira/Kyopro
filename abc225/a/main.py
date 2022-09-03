S = input()
se = set()
for s in S:
    se.add(s)

if len(se) == 1:
    print(1)
elif len(se) == 2:
    print(3)
else:
    print(6)