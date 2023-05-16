def get_possible_numbers(length):
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [-1, 0, -1]
    ]

    # Initialize the DP table with 0's
    dp = [[0] * 10 for _ in range(length + 1)]

    # Initialize the DP table for length 1
    for i in range(10):
        dp[1][i] = 1

    # Populate the DP table for lengths greater than 1
    for l in range(2, length + 1):
        for i in range(10):
            for j in keypad[i]:
                if j != -1:
                    dp[l][i] += dp[l - 1][j]

    # Sum all the possibilities for the given length
    total_possibilities = 0

    # Iterate over the last digit possibilities
    for i in range(10):
        total_possibilities += dp[length][i]

    return total_possibilities


# Read the input value
length = int(input())

# Calculate and print the possible numbers
print(get_possible_numbers(length))