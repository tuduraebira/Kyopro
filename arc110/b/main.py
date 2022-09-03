N = int(input())
T = input()
S = "110" * (N // 3 + 3)

if T in S:
    if T == "1":
        print(2 * (10 ** 10))
    elif T == "11":
        print(10 ** 10)
    else:
        K = T.count("0")

        if T[-1] == "0":
            print(10 ** 10 - K + 1)
        else:
            print(10 ** 10 - K)
else:
    print(0)
