#Write a Python program to implement a binary search algorithm.

def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        # Calculate the middle index
        mid = (start + end) // 2
        
        # Check if the target is found at the mid index
        if arr[mid] == target:
            return mid  # Target found, return the index
        # If the target is smaller than the middle element, search in the left half
        elif arr[mid] > target:
            end = mid - 1
        # If the target is greater than the middle element, search in the right half
        else:
            start = mid + 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9

result = binarySearch(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")