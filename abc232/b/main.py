S = input()
T = input()

if S == T:
    print("Yes")
    exit()
elif ord(S[0]) > ord(T[0]):
    num = ord(S[0]) - ord(T[0])

    ans = S[0]
    for c in T[1:]:
        ans += chr(ord('a') + ((ord(c) - ord('a') + num) % 26))
    if ans == S:
        print("Yes")
    else:
        print("No")
else:
    num = ord(T[0]) - ord(S[0])

    ans = T[0]
    for c in S[1:]:
        ans += chr(ord('a') + ((ord(c) - ord('a') + num) % 26))
    if ans == T:
        print("Yes")
    else:
        print("No")