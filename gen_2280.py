#!/usr/bin/env python3
"""Generate compact mov code for printf (2280)"""

print("# 2280 - printf")
print("")

# Read input
print("A<I")
print("")

# Strategy: Output three digits, using 0 (no output) for leading positions

# Hundreds digit
print("# Hundreds lookup")
for i in range(256):
    s = str(i)
    if len(s) >= 3:
        h = ord(s[0])
    else:
        h = 0
    print(f"[{i}]<{h}")
print("")

print("H<[A]")
print("O<H")
print("")

# Tens digit - needs different memory offset
# Since we can't compute A+256, store tens at specific offset
# and use double indirection

# Approach: create pointer table
# mem[i] = position where tens digit for value i is stored
positions_start = 300
print("# Pointer table for tens digit positions")
for i in range(256):
    print(f"[{i}]<{positions_start + i}")
print("")

# Store actual tens digits at those positions
print("# Tens digit data")
for i in range(256):
    s = str(i)
    if len(s) >= 2:
        t = ord(s[-2])
    else:
        t = 0
    pos = positions_start + i
    if pos < 512:  # Memory limit check
        print(f"[{pos}]<{t}")
print("")

# But this still overflows memory...
# Memory is only 512 bytes

# Let me use a different approach: reuse memory after reading
# After getting hundreds, overwrite that memory with tens data
print("# Overwrite with tens data")
for i in range(256):
    s = str(i)
    if len(s) >= 2:
        t = ord(s[-2])
    else:
        t = 0
    print(f"[{i}]<{t}")
print("")

print("T<[A]")
print("O<T")
print("")

# Same for ones
print("# Overwrite with ones data")
for i in range(256):
    s = str(i)
    o = ord(s[-1])
    print(f"[{i}]<{o}")
print("")

print("P<[A]")
print("O<P")
print("")

print("Z<1")
