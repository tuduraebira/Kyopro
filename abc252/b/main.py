from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ind = defaultdict(list)
for i, a in enumerate(A):
    ind[a].append(i + 1)

ind_sort = sorted(ind.items(), reverse=True)
for l in ind_sort[0][1]:
    if l in B:
        print("Yes")
        exit()

print("No")