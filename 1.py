def find_missing_integer(n, sequence):
    # Calculate the common difference
    diff = (sequence[-1] - sequence[0]) // n

    # Iterate through the sequence and check for missing integer
    for i in range(1, n):
        if sequence[i] - sequence[i-1] != diff:
            return sequence[i-1] + diff

    # If no missing integer found
    return None

# Read input values
print("Masukan Jumlah Bilangan")
n = int(input())
print("Masukan Bilangan")
sequence = list(map(int, input().split()))

# Find the missing integer
print("output")
missing_integer = find_missing_integer(n, sequence)

# Print the missing integer
print(missing_integer)