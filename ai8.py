import numpy as np

# All 8 possible bipolar patterns
patterns = np.array([
    [ 1,  1,  1],
    [ 1,  1, -1],
    [ 1, -1,  1],
    [ 1, -1, -1],
    [-1,  1,  1],
    [-1,  1, -1],
    [-1, -1,  1],
    [-1, -1, -1]
])

# Take input from user
print("Enter a bipolar pattern (only 1 or -1):")

x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
x3 = int(input("Enter x3: "))

input_pattern = np.array([x1, x2, x3])

# Associative recall
recalled_pattern = None

for pattern in patterns:
    if np.array_equal(input_pattern, pattern):
        recalled_pattern = pattern
        break

print("\nInput pattern    :", input_pattern)
print("Recalled pattern :", recalled_pattern)

if np.array_equal(input_pattern, recalled_pattern):
    print("Status: Pattern recalled successfully")
else:
    print("Status: Pattern not found")
