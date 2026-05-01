import sys
side = int(sys.stdin.read().strip())
surface_area = 6 * side * side
volume = side * side * side
print(f"Surface area = {surface_area} and Volume = {volume}")
