def min_steps_to_equalize(n, a, b):
    # Check if it is possible to make all a's equal
    if sum(a) != n * a[0]:
        return -1
    
    steps = 0
    
    # Iterate until all a's are equal
    while len(set(a)) > 1:
        # Calculate the minimum value among a[i]-b[i] for each i
        min_diff = min(ai - bi for ai, bi in zip(a, b))
        
        # Update the values of a[i] and increment the steps count
        for i in range(n):
            a[i] -= min_diff
            steps += 1
    
    return steps


# Read the input values
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate and print the minimum number of steps
print(min_steps_to_equalize(n, a, b))