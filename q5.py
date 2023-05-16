def max_packets(r, g, b):
    # Sort the balls in descending order
    balls = sorted([r, g, b], reverse=True)

    # Calculate the maximum number of packets
    max_packets = min(balls[0], (balls[1] + balls[2])) + min(balls[1], balls[2])

    return max_packets

# Input values
r, g, b = 5, 4, 3

# Calculate the maximum number of packets
result = max_packets(r, g, b)

# Print the result
print(result)