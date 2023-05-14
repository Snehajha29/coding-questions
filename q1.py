import math

# Read the input string
input_str = input()

# Parse the input string
m, op, n = input_str.split("#")
m = int(m)
n = int(n)

# Evaluate the arithmetic operation
if op == "+":
    result = m + n
elif op == "-":
    result = m - n
elif op == "*":
    result = m * n
elif op == "/":
    result = m / n

# Take the floor of the result
result = math.floor(result)

# Print the result
print(result)
