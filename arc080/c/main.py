N = int(input())
a = list(map(int, input().split()))

cnt4 = 0
cnt2 = 0
cntel = 0
for n in a:
    if n % 4 == 0:
        cnt4 += 1
    elif n % 2 == 0:
        cnt2 += 1
    else:
        cntel += 1

if cnt2:
    nokori = N - cnt2
    if nokori % 2 == 0:
        if cnt4 >= nokori // 2:
            print("Yes")
        else:
            print("No")
    else:
        if cnt4 >= nokori // 2 + 1:
            print("Yes")
        else:
            print("No")
else:
    if cnt4 >= N // 2:
        print("Yes")
    else:
        print("No")