N = int(input())
S = input()

xsum, m = 0, 0
for i in range(1, N - 1):
    if S[i - 1:i + 2] == 'ARC':
        l, r = i - 1, i + 1
        while l - 1 >= 0 and S[l - 1] == 'A':
            l -= 1
        while r + 1 < N and S[r + 1] == 'C':
            r += 1
        
        x = min(i - l, r - i)
        xsum += x
        m += 1

print(min(xsum, m * 2))