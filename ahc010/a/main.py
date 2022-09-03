from random import randint


t = [input() for _ in range(30)]

ans = ""
for _ in range(900):
    ans += str(randint(0, 3))

print(ans)