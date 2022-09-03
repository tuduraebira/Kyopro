K, A, B = map(int, input().split())

ans = 1
if A + 1 >= B:
    ans += K
    print(ans)
    exit()
else:
    cnt = K
    if ans < A:
        sa = A - ans
        ans += sa
        cnt -= sa

    #print(cnt)
    if cnt % 2 == 0:
        ans += (B - A) * cnt // 2
    else:
        ans += ((B - A) * (cnt // 2))
        ans += 1

print(ans)