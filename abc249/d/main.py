from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

yakusuu = []
cnt = defaultdict(int)
for a in A:
    cnt[a] += 1
    yakusuu.append(make_divisors(a))
#print(cnt)
#print(yakusuu)

ans = 0
s = set()
for i in range(N):
    ai = A[i]
    if ai not in s:
        for aj in yakusuu[i]:
            if cnt.get(ai / aj) != None:
                #print(ai, aj)
                ans += cnt[ai] * cnt[aj] * cnt[ai / aj]
    s.add(ai)

print(ans)