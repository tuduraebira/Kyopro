A, B, C, D = map(int, input().split())

def check_prime(num):
    half = num // 2
    count = 0

    for i in range(2, half+1):
        if num % i == 0:
            count += 1
    
    if count == 0:
        return True
    else:
        return False

for i in range(A, B+1):
    is_Aoki_win = False

    for j in range(C, D+1):
        if check_prime(i + j):
            is_Aoki_win = True
            break
    
    if not is_Aoki_win:
        print("Takahashi")
        exit()

print("Aoki")