M, N = map(int, input().split())
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
lcm = (M * N) // gcd(M, N)
print(lcm)
