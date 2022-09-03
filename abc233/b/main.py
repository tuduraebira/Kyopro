L, R = map(int, input().split())
S = input()

s_fw = S[:L-1]
s_rev = S[L-1:R]
s_bw = S[R:]

print(s_fw + s_rev[::-1] + s_bw)