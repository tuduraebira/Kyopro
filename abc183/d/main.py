from collections import defaultdict


N, W = map(int, input().split())
start = defaultdict(list)
end = defaultdict(list)
for _ in range(N):
    S, T, P = map(int, input().split())
    start[S].append(P)
    end[T].append(P)

wa = 0
for i in range(200001):
    if start.get(i) != None:
        wa += sum(start[i])
    if end.get(i) != None:
        wa -= sum(end[i])

    if wa > W:
        print("No")
        exit()

print("Yes")