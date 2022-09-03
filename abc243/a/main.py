v, a, b, c = map(int, input().split())

use = 0
while True:
    use += a
    if v - use < 0:
        print("F")
        exit()

    use += b
    if v - use < 0:
        print("M")
        exit()

    use += c
    if v - use < 0:
        print("T")
        exit()