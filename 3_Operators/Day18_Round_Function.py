print(round(7))         # 7
# Already an integer

print(round(7.61))      # 8
# Nearest integer

print(round(2.66666, 2))    # 2.67
# 3rd digit ≥ 5

print(round(2.66234, 2))    # 2.66
# 3rd digit < 5

print(round(2.6663, 3))     # 2.666
# 4th digit < 5

print(round(2.6668, 3))     # 2.667
# 4th digit ≥ 5

print(round(674, 2))    # 674
# No decimals

print(round(2.66457, 0))    # 3.0
# 0 decimal places

print(round(6.5))       # 6
print(round(7.5))       # 8
# Nearest even

print(round(2.25, 1))   # 2.2
print(round(2.35, 1))   # 2.4
# Tie → nearest even

print(round(-1.5))      # -2
# Nearest even

print(round(674, -1))   # 670
print(round(674, -2))   # 700
print(round(1674, -3))  # 2000
# Nearest 10, 100, 1000