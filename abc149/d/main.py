N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

pre = ['a'] * K

ans = 0
for i, t in enumerate(T):
    pt = i % K
    if t == 'r' and pre[pt] != 'p':
        ans += P
        pre[pt] = 'p'
    elif t == 's' and pre[pt] != 'r':
        ans += R
        pre[pt] = 'r'
    elif t == 'p' and pre[pt] != 's':
        ans += S
        pre[pt] = 's'
    else:
        pre[pt] = 'a'

print(ans)