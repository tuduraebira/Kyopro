hw = list(map(int, input().split()))

ans = 0
oo = 1
while True:
    if hw[0] - 2 < oo or hw[3] - 2 < oo:
        break
    
    res_oo = hw[0] - oo
    ot = 1
    while True:
        if res_oo - 2 < ot or hw[4] - 2 < ot:
            break

        res_ot = hw[3] - oo
        to = 1
        while True:
            if hw[1] - 2 < to or res_ot - 2 < to:
                break

            res_to = hw[4] - ot
            res_tt = hw[1] - to
            tt = 1
            while True:
                if res_tt - 2 < tt or res_to - 2 < tt:
                    break
                print(oo, ot, to, tt)

                ans += 1
                tt += 1
            to += 1
        ot += 1
    oo += 1

print(ans)