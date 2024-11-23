# Write a Python program to find the median of a list of numbers.

def findMedianNumber():
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1:
        median = sorted_numbers[length // 2]
    else:
        #One Approch
        mid1 = sorted_numbers[length // 2 - 1]
        mid2 = sorted_numbers[length // 2]
        median = (mid1 + mid2) / 2
        
        #Second Approach
        # print((length+1)/2, length, (length + 1)/2) 
    return median


numbers = [3, 5, 1,6,7, 4, 2, 8,9,10]

print(f"The median is: {findMedianNumber()}")