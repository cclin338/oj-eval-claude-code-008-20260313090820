#!/usr/bin/env python3
"""Generate mov code for printf (2280) - no null bytes"""

print("# 2280 - printf v4")
print("")

# Read input
print("A<I")
print("")

# Create a lookup table that maps each value to a sequence of outputs
# For value i: create sequence of non-zero bytes ending in a specific marker

# Use mem[300-399] to store count of digits for each common value
# Then mem[400+] to store the actual digits

print("# Digit count lookup (1-3)")
for i in range(256):
    count = len(str(i))
    print(f"[{i}]<{count}")
print("")

print("C<[A]")  # C = count of digits
print("")

# Create lookup for first digit
print("# First digit (or 0 if count < 3)")
for i in range(256):
    s = str(i)
    d1 = ord(s[0]) if len(s) >= 1 else 0
    print(f"[{i}]<{d1}")
print("")

# For count=3: output first digit
print("# If count==3, output first digit")
print("[3]<1")
print("[2]<0")
print("[1]<0")
print("F<[C]")
print("Z<F")  # Halt if count!=3
print("D<[A]")
print("O<D")
print("Z<0")  # Clear Z
print("")

# For count>=2: output second digit
# Overwrite lookup
print("# Second digit")
for i in range(256):
    s = str(i)
    if len(s) >= 2:
        d2 = ord(s[-2])  # second-to-last
    elif len(s) == 1:
        d2 = 0
    else:
        d2 = 0
    print(f"[{i}]<{d2}")
print("")

print("[2]<1")
print("[3]<1")
print("[1]<0")
print("F<[C]")
print("Z<F")
print("E<[A]")
print("O<E")
print("Z<0")
print("")

# Always output last digit
print("# Last digit (ones)")
for i in range(256):
    s = str(i)
    d3 = ord(s[-1])
    print(f"[{i}]<{d3}")
print("")

print("G<[A]")
print("O<G")
print("")

print("Z<1")
