def reverse_kth_rows(matrix, k):
    if k <= 0:
        print("Invalid value of k")
        return

    for i in range(k - 1, len(matrix), k):
        matrix[i] = matrix[i][::-1]

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]

k = 3

print("Original Matrix:")
for row in matrix:
    print(row)

reverse_kth_rows(matrix, k)

print("\nMatrix after reversing every", k, "th row:")
for row in matrix:
    print(row)
