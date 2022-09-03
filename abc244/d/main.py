S1, S2, S3 = map(str, input().split())
T1, T2, T3 = map(str, input().split())

ok = [[S1, S2, S3], [S3, S1, S2], [S2, S3, S1]]
no = [[S1, S3, S2], [S3, S2, S1], [S2, S1, S3]]

for l in ok:
    if T1 == l[0] and T2 == l[1] and T3 == l[2]:
        print("Yes")
        exit()
print("No")