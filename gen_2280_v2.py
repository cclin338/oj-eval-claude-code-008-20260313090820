#!/usr/bin/env python3
"""Generate compact mov code for printf (2280) - avoiding null output"""

print("# 2280 - printf v2")
print("")
print("A<I")
print("")

# Strategy: Create lookup tables but use control flow to avoid O<0
# Store lookup flag: if digits should be output
# mem[i] = 1 if we should output hundreds for value i, 0 otherwise

print("# Hundreds digit lookup - 1 if should output, 0 if not")
for i in range(256):
    should_output = 1 if i >= 100 else 0
    print(f"[{i}]<{should_output}")
print("")

print("H<[A]")
print("# Check if H==1, then output")
print("[0]<0")  # Don't halt
print("[1]<1")  # Halt to skip if 0
print("Z<[H]")  # Halt if H==0
print("")

# If we're here, H==1, so output hundreds
print("# Overwrite with hundreds ASCII values")
for i in range(256):
    h_digit = i // 100
    print(f"[{i}]<{48 + h_digit}")
print("")
print("B<[A]")
print("O<B")
print("Z<0")  # Reset Z
print("")

# Continue with tens...
# Actually this approach breaks the program flow

# Let me use a different approach: use a state machine
# State 0: check and output hundreds
# State 1: check and output tens
# State 2: output ones
# State 3: halt

print("Z<1")
