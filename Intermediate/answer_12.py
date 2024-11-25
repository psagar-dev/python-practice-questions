#Write a Python program to find the maximum subarray sum in a given list of integers.

def maxSubarraySum(nums):
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

input_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4, -1,11,15,20]

print("Maximum Subarray Sum: ", maxSubarraySum(input_nums))