S = list(input())
a, b = map(int, input().split())

tmp_a = S[a - 1]
S[a - 1] = S[b - 1]
S[b - 1] = tmp_a

print(''.join(S))