N = int(input())

if N >= 42:
    print(f"AGC0{N + 1}")
elif N < 10:
    print(f"AGC00{N}")
else:
    print(f"AGC0{N}")