def find_next_greater(n):
    # Convert the integer to a list of digits
    digits = list(str(n))
    
    # Find the first digit from the right that is smaller than its right neighbor
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # If no such digit is found, there is no valid output
    if i < 0:
        return -1
    
    # Find the smallest digit to the right of digits[i] that is larger than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]
    
    # Reverse the digits to the right of i to get the smallest possible number
    digits[i + 1:] = digits[i + 1:][::-1]
    
    # Convert the list of digits back to an integer
    next_greater = int(''.join(digits))
    
    # Check if the next greater number fits in a 32-bit integer
    if next_greater > 2**31 - 1:
        return -1
    
    return next_greater


# Read the input value
#n = int(input(112))

# Find the next greater number and print the result
print(find_next_greater(112))