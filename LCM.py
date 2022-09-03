from math import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)