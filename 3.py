def count_brick_wall_patterns(length):
    # Create a list to store the number of patterns for each wall length
    patterns = [0] * (length + 1)

    # Base cases
    patterns[0] = 1  # There is one pattern for a wall of length 0
    patterns[1] = 1  # There is one pattern for a wall of length 1

    # Calculate the number of patterns for wall lengths from 2 to the given length
    for i in range(2, length + 1):
        patterns[i] = patterns[i - 1] + patterns[i - 2]

    return patterns[length]


# Read the wall lengths from the input until a '0' is encountered
input_string = input()
wall_lengths = list(map(int, input_string.split()))

# Calculate and print the number of different patterns for each wall length
for length in wall_lengths:
    if length == 0:
        break
    patterns = count_brick_wall_patterns(length)
    print(patterns)
