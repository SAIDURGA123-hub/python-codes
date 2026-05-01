import sys
data = list(map(int, sys.stdin.read().split()))
a, b = data[0], data[1]
a, b = b, a
print(a)
print(b)
