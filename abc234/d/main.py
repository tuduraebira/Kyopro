from heapq import heapify, heappush, heappop

N, K = map(int, input().split())
P = list(map(int, input().split()))

pq = P[:K]
heapify(pq)
print(pq[0])

for x in P[K:]:
    heappush(pq, x)
    heappop(pq)
    print(pq[0])