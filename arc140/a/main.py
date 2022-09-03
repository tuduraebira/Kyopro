N, K = map(int, input().split())
S = input()

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

ans = N
yakusuu = make_divisors(N)

for num in yakusuu:
    kakikae = 0
    cnt = [[0] * 26 for _ in range(num)]
    #print(cnt)

    for i in range(len(S)):
        amari = i % num
        cnt[amari][ord(S[i]) - 97] += 1
    
    #print(cnt)

    for c in cnt:
        kakikae += ((N // num) - max(c))

    if kakikae <= K:
        ans = min(ans, num)

print(ans)