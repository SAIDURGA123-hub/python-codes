import sys
data = list(map(float, sys.stdin.read().split()))
base1, base2, height = data[0], data[1], data[2]
area = 0.5 * (base1 + base2) * height
print(f"{area:.4f}")
