N = int(input())
S = [input() for _ in range(N)]
s_dict = {}

for s in S:
    if s_dict.get(s) != None:
        print(s + '(' + str(s_dict[s]) + ')')
        s_dict[s] += 1
    else:
        print(s)
        s_dict[s] = 1