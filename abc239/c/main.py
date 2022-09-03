x1, y1, x2, y2 = map(int, input().split())

kumi = [[x1 - 2, y1 - 1], [x1 + 2, y1 - 1], [x1 - 2, y1 + 1], [x1 + 2, y1 + 1],
        [x1 - 1, y1 - 2], [x1 + 1, y1 - 2], [x1 - 1, y1 + 2], [x1 + 1, y1 + 2]]
for k in kumi:
    if (x2 - k[0]) ** 2 + (y2 - k[1]) ** 2 == 5:
        print("Yes")
        exit()
print("No")