import sys
import math
data = list(map(float, sys.stdin.read().split()))
P, R, T = data[0], data[1], data[2]
A =P * (1 + R/100) ** T
CI = A - P
print(f"{CI:.2f}")
