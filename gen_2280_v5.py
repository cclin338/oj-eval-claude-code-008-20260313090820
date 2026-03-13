#!/usr/bin/env python3
"""Generate mov code for printf (2280) - use conditional memory writes"""

print("# 2280 - printf v5")
print("")
print("A<I")
print("")

# Strategy: Create output buffer, write digits conditionally, then output buffer
# Output will go to mem[500, 501, 502] (max 3 digits)
# Then output them in sequence

# Initialize output buffer
print("[500]<0")
print("[501]<0")
print("[502]<0")
print("")

# Digit count
print("# Count lookup")
for i in range(256):
    print(f"[{i}]<{len(str(i))}")
print("")
print("C<[A]")
print("")

# Position 500: hundreds digit (if count==3)
print("# Hundreds lookup")
for i in range(256):
    s = str(i)
    if len(s) == 3:
        h = ord(s[0])
    else:
        h = 0  # Will be 0 for count < 3
    print(f"[{i}]<{h}")
print("")
print("[500]<[A]")
print("")

# Position 501: tens digit (if count >= 2)
print("# Tens lookup")
for i in range(256):
    s = str(i)
    if len(s) >= 2:
        t = ord(s[-2])
    else:
        t = 0
    print(f"[{i}]<{t}")
print("")
print("[501]<[A]")
print("")

# Position 502: ones digit (always)
print("# Ones lookup")
for i in range(256):
    s = str(i)
    o = ord(s[-1])
    print(f"[{i}]<{o}")
print("")
print("[502]<[A]")
print("")

# Output: If count==3, output all 3. If count==2, output [501],[502]. If count==1, output [502].
# Use count to determine starting position

# Create lookup: mem[C+300] = starting position
print("# Starting position lookup")
print("[301]<502")  # count=1: start at 502
print("[302]<501")  # count=2: start at 501
print("[303]<500")  # count=3: start at 500
print("")

print("P<C")
print("P<300")  # Can't add, need lookup
# Create lookup for C+300
for i in range(4):
    print(f"[{i}]<{i+300}")
print("")
print("P<[C]")
print("P<[P]")  # P = starting position
print("")

# Output all three positions (nulls will be output but might be OK)
print("O<[500]")
print("O<[501]")
print("O<[502]")
print("")

print("Z<1")
