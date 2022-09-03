N, A, B = map(int, input().split())

if N < A:
    print(0)
elif A <= B:
    print(N - A + 1)
else:
    res = N - A + 1
    loop = res // A
    amari = res % A

    ans = loop * B
    if amari > B:
        ans += B
    else:
        ans += amari

    print(ans)