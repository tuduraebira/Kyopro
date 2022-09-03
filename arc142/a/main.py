N, K = map(int, input().split())

ans = set()
if K <= int(str(K)[::-1]):
    sK = K
    srK = int(str(K)[::-1])
    while True:
        if sK > N and srK > N:
            break

        if 1 <= sK and sK <= N:
            ans.add(sK)
        if 1 <= srK and srK <= N:
            ans.add(srK)
        sK *= 10
        srK *= 10
else:
    pass

print(len(ans))