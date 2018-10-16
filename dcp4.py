# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive
# integer in linear time and constant space.
#  In other words, find the lowest
# positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#You can modify the input array in-place.


#Attempt 1: Not linear, uses a for loop with a recursive call to a helper function. the helper function is called n times,
# and is first invoked in the body of a for loop that iterates n times, need more efficient approach
# global_counter_time_comp = 0

# def dcp4(in_array):
#     global global_counter_time_comp
#     for num in in_array:
#         global_counter_time_comp += 1
#         print("For Loop: counter = "< str(global_counter_time_comp))
#         if num > 0:
#             all_included, num_missing = dcp4_helper(num,in_array)
#             if not all_included:
#                 return num_missing,global_counter_time_comp
#
#
#
# # define helper function to recursively check if num - 1 is in the array, the "in" is constant time
# def dcp4_helper(num, in_array):
#     global global_counter_time_comp
#     global_counter_time_comp += 1
#     print("Recursive call: counter = " < str(global_counter_time_comp))
#     if num == 0:
#         return True,None
#     if num not in in_array:
#         return False,num
#     if num in in_array:
#         return dcp4_helper(num - 1, in_array)
#
# print(dcp4([3, 4, -1, 1]))
# print(dcp4([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]))

# Attempt 2
# segregate the list into positive and negatives, we only care about positive numbers
# traverse the sub list of positives. to mark that a number a[i] has been visited, make arr[arr[i] - 1] negative
# traverse again, return first index with a positive value
import math

def segregate(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] <= 0:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j += 1
    return j
def findMissingPositive(nums):

    for i in range(len(nums)):
        x = abs(nums[nums[i] - 1])
        if x < len(nums) and x > 0:
            nums[nums[i] - 1] = - x

    for i in range(len(nums)):
        if nums[i+1] > 0:
            return i + 1
    return len(nums) + 1

def findMissing(nums):
    shift = segregate(nums)
    findMissingPositive(nums[shift:])

print(segregate([1,2,3,4,5,-6,7,8,9,10,-11,-12,13,-14,15,16,-17,18,-20]))
