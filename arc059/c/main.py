from decimal import Decimal, ROUND_HALF_UP

N = int(input())
a = list(map(int, input().split()))

average = Decimal(str(sum(a))) / Decimal(str(N))
y = average.quantize(Decimal('0'), rounding=ROUND_HALF_UP)

ans = 0
for n in a:
    ans += (n - y) ** 2

print(ans)