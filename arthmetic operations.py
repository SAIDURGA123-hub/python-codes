import sys
data = list(map(int, sys.stdin.read().split()))
num1, num2 = data[0], data[1]
print(f"Sum:{num1 + num2}")
print(f"Difference:{num1 - num2}")
print(f"Product:{num1 * num2}")
print(f"Quotient:{num1 // num2}")
print(f"Remainder:{num1 % num2}")
