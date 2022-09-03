from collections import defaultdict


N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

K = 0
ans = set()
for bi in b:
    isNum = defaultdict(int)
    for n in b:
        isNum[str(n)] += 1

    isNum[str(bi)] -= 1
    good_num = a[0] ^ bi

    for i in range(1, N):
        b_xor = a[i] ^ good_num
        if isNum[str(b_xor)] <= 0:
            break
        else:
            isNum[str(b_xor)] -= 1

        if i == N - 1:
            K += 1
            ans.add(good_num)

print(len(ans))
aans = sorted(ans)
for n in aans:
    print(n)