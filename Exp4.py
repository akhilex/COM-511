# Linear Search Function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search Function (Assuming the array is sorted)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Main function
def main():
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target = 12

    # Perform Linear Search
    linear_result = linear_search(arr, target)
    if linear_result != -1:
        print(f"Linear Search: Element {target} found at index {linear_result}")
    else:
        print(f"Linear Search: Element {target} not found in the array")

    # Perform Binary Search
    binary_result = binary_search(arr, target)
    if binary_result != -1:
        print(f"Binary Search: Element {target} found at index {binary_result}")
    else:
        print(f"Binary Search: Element {target} not found in the array")

if __name__ == "__main__":
    main()
