a, b, n = map(int, input().split())

def cnt_seven(N):
    N = str(N)
    length = len(N)

    dp = [[[0] * 2 for _ in range(2)] for _ in range(length + 1)]
    dp[0][0][0] = 1

    for i in range(length):
        max_digit = int(N[i])

        for flag_less in range(2):
            for flag_seven in range(2):
                range_digit = 9 if flag_less else max_digit
                for d in range(range_digit + 1):
                    flag_less_next = 0
                    flag_seven_next = 0
                    if flag_less == 1 or d < max_digit:
                        flag_less_next = 1
                    if flag_seven == 1 or d == 7:
                        flag_seven_next = 1
                    dp[i + 1][flag_less_next][flag_seven_next] += dp[i][flag_less][flag_seven]

    return dp[length][0][1] + dp[length][1][1]

left = -1
right = 10 ** 12 + 10
while right - left > 1:
    mid = (left + right) // 2
    if a * mid + b * cnt_seven(mid) + a < n:
        left = mid
    else:
        right = mid
    #print(mid, a * mid + b * cnt_seven(mid))

print(left, right)

# a, b, n = map(int, input().split())

# point = a
# ans = 0
# while point < n:
#     ans += 1
#     point += a
#     if str(ans).count('7') > 0:
#         point += b

# print(ans)