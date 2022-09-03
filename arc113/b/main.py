A, B, C = map(int, input().split())

BC = pow(B, C, 4)
if BC == 0:
    BC = 4
ans = pow(A, BC, 10)
print(ans)