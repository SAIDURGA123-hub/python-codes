CP, SP = map(int, input().split())
loss_percentage = ((CP - SP) / CP) * 100
print(f"{loss_percentage:.2f}")
