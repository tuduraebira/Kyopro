N = int(input())
is_num = [False] * ((2 * N + 1) + 1)

pt = 1
while True:
    while True:
        if is_num[pt] == False:
            print(pt, flush=True)
            is_num[pt] = True
            break
        else:
            pt += 1
    
    aoki = int(input())
    is_num[aoki] = True

    if aoki == 0:
        exit()