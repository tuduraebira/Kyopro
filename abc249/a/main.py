A, B, C, D, E, F, X = map(int, input().split())

ta = 0
ao = 0
time = 0
yasumi = False
while time < X:
    if not yasumi:
        time += A
        ta += (A * B)
        yasumi = True
    else:
        time += C
        #ta = A * B
        yasumi = False
    #print(time, ta)
if yasumi:
    ta -= (time - X) * B

time = 0
yasumi = False
while time < X:
    if not yasumi:
        time += D
        ao += (D * E)
        yasumi = True
    else:
        time += F
        #ta = A * B
        yasumi = False
    #print(time, ao)
if yasumi:
    ao -= (time - X) * E

if ta == ao:
    print("Draw")
elif ta > ao:
    print("Takahashi")
else:
    print("Aoki")    
