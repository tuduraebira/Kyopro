N = int(input())
P = list(map(int, input().split()))

ans = []
for i in range(N):
    if i + 1 != N:
        if i % 2 == 0 and P[i] % 2 == 0 or i % 2 == 1 and P[i] % 2 == 1:
            if (i + 1) % 2 == 0 and P[i + 1] % 2 == 0 or (i + 1) % 2 == 1 and P[i + 1] % 2 == 1:
                P[i], P[i + 1] = P[i + 1], P[i]
                ans.append(('A', i + 1))
            else:
                ind = -1
                for j in range(i + 1, N, 2):
                    if j % 2 == 0 and P[j] % 2 == 0 or j % 2 == 1 and P[j] % 2 == 1:
                        ind = j
                
                cnt = (ind - i) // 2
                for _ in range(cnt):
                    P[ind - 2], P[ind] = P[ind], P[ind - 2]
                    ans.append(('B', ind - 1))
                    ind -= 2
                P[i], P[i + 1] = P[i + 1], P[i]
                ans.append(('A', i + 1))

#print(P)
# cor = 0
# for i in range(N):
#     if i % 2 == 0:
#         if P[i] % 2 == 1:
#             cor += 1
#             continue
#         else:
#             if i == 0:
#                 continue
#             else:
#                 cnt = i // 2
#                 ind = i
#                 for _ in range(cnt):
#                     P[ind - 2], P[ind] = P[ind], P[ind - 2]
#                     ans.append(('B', ind - 1))
#                     ind -= 2
#     else:
#         if P[i] % 2 == 0:
#             cor += 1
#             continue
#         else:
#             if i == 1:
#                 continue
#             else:
#                 cnt = i // 2
#                 ind = i
#                 for _ in range(cnt):
#                     P[ind - 2], P[ind] = P[ind], P[ind - 2]
#                     ans.append(('B', ind - 1))
#                     ind -= 2

# cntA = (N - cor) // 2
# j = 0
# for _ in range(cntA):
#     P[j], P[j + 1] = P[j + 1], P[j]
#     ans.append(('A', j + 1))
#     j += 2

for k in range(N):
    num = k + 1
    ind = P.index(num)
    if ind + 1 == num:
        continue
    elif ind + 1 > num:
        cnt = ((ind + 1) - num) // 2
        i = ind
        for _ in range(cnt):
            P[i - 2], P[i] = P[i], P[i - 2]
            ans.append(('B', i - 1))
            i -= 2
    else:
        cnt = (num - (ind + 1)) // 2
        i = ind
        for _ in range(cnt):
            P[i + 2], P[i] = P[i], P[i + 2]
            ans.append(('B', i + 1))
            i += 2

print(len(ans))
for c, i in ans:
    print(c, i)
#print(P)