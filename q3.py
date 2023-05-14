# right code

def find_largest_possible_integer(N):
    # Convert N to string for easier manipulation
    N_str = str(N)

    # Initialize max_digit and max_index
    max_digit = N_str[0]
    max_index = 0

    # Traverse the string to find the maximum digit and its index
    for i in range(1, len(N_str)):
        if N_str[i] > max_digit:
            max_digit = N_str[i]
            max_index = i

    # If the maximum digit is already at the leftmost position, no swaps needed
    if max_index == 0:
        return N

    # Traverse the string again to find the leftmost smaller digit
    for i in range(max_index):
        if N_str[i] < max_digit:
            swap_index = i
            break

    # Swap the digits at max_index and swap_index
    N_list = list(N_str)
    N_list[max_index], N_list[swap_index] = N_list[swap_index], N_list[max_index]

    # Convert the modified string back to integer and return it
    return int("".join(N_list))
print(find_largest_possible_integer(210))