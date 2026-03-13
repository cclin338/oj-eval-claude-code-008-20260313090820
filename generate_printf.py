#!/usr/bin/env python3
"""Generate mov code for printf problem (2280)"""

# Strategy: Create direct lookup tables
# For each value 0-255, pre-compute its decimal representation
# and store where to find it

print("# 2280 - printf")
print("# Read character and output ASCII code in decimal")
print()

# Store decimal representations in memory starting at position 300
# Format: each number's digits stored sequentially
# e.g., "57" stored as [300]: 5+48=53, [301]: 7+48=55, [302]: 0 (terminator)

# Create a mapping: mem[input_value] = starting position of its decimal string

# First, generate all decimal representations
representations = {}
pos = 300
for i in range(256):
    s = str(i)
    representations[i] = pos
    pos += len(s) + 1  # +1 for terminator

print("# Initialize lookup table: mem[i] = position of decimal string for value i")
for i in range(256):
    print(f"[{i}]<{representations[i]}")
print()

print("# Initialize decimal string data")
for i in range(256):
    s = str(i)
    pos = representations[i]
    for digit_char in s:
        print(f"[{pos}]<{ord(digit_char)}")
        pos += 1
    print(f"[{pos}]<0")  # Terminator
print()

print("# Read input")
print("A<I")
print()

print("# Get starting position of decimal string")
print("P<[A]")
print()

print("# Output digits until terminator")
print("# We need a loop, but program loops automatically")
print("# Use register C as position offset")
print("C<P")
print()

print("# Output character at position C")
print("D<[C]")
print()

print("# Check if D is 0 (terminator)")
print("[0]<1")  # mem[0] = 1 (halt flag)
print("E<[D]")  # E = mem[D], which is 1 if D=0, else 0
print("Z<E")    # Halt if E=1
print()

print("# Output D")
print("O<D")
print()

print("# Increment C (using lookup table)")
for i in range(300, 512):
    print(f"[{i}]<{i+1}")
print("C<[C]")
print()

# Program loops, so it will continue outputting until terminator
