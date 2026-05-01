import sys
data = list(map(float, sys.stdin.read().split()))
salary, hra, da = data[0], data[1], data[2]
pf = 0.12 * salary
gross_salary = salary + hra + da + pf
print(f"{pf:.2f}")
print(f"{gross_salary:.2f}")
