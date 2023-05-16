def max_packets(r, g, b):
    # Find the maximum number of packets that can be made
    # by distributing the balls evenly among the packets
    
    # Sort the counts of balls in descending order
    counts = sorted([r, g, b], reverse=True)
    
    # Calculate the maximum number of packets
    packets = (counts[0] // 3) + (counts[1] // 3) + (counts[2] // 3)
    
    # Handle the case where there are leftover balls
    if min(counts) >= 1:
        leftovers = [counts[0] % 3, counts[1] % 3, counts[2] % 3]
        min_leftovers = min(leftovers)
        
        # Check if there are enough leftover balls to form another packet
        if min_leftovers >= 1 and sum(leftovers) >= 3:
            packets += 1
    
    return packets


# Read the input values
r, g, b = map(int, input().split())

# Calculate and print the maximum number of packets
print(max_packets(r, g, b))