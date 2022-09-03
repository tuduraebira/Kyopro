def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

T = int(input())
for _ in range(T):
    N = input()

    l = make_divisors(len(N))
    l = l[:-1]
    
    ans = -1
    for n in l:
        result = [N[idx:idx + n] for idx in range(0,len(N), n)]
        #print(result)

        isok = True
        for i in range(1, len(result)):
            if int(result[0]) == int(result[i]):
                continue
            else:
                if int(result[0]) > int(result[i]):
                    isok = False
                else:
                    isok = True
                break
        
        #print(int(str(int(result[0]) - 1)))
        #print('1', int(str(int(result[0]) - 1) * len(result)))
        if isok:
            tmp = result[0] * len(result)
            ans = max(ans, int(tmp))
        else:
            tmp = str(int(result[0]) - 1) * len(result)
            ans = max(ans, int(tmp))
        if int(tmp) == 0:
            ans = max(ans, 10 ** (len(tmp) - 1) - 1)
        #print(ans)
    
    print(ans)