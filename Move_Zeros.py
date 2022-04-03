"""
Question: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

def moveZerores(nums):
    prev = -1
    for i in range(len(nums)):
        if nums[i] == 0 and prev == -1:
            prev = i
        elif nums[i] != 0 and prev != -1:
            nums[i], nums[prev] = nums[prev], nums[i]
            prev += 1

test1 = [0, 1, 0, 3, 12]
test2 = [1, 0, 0, 2, 0, 3]
test3 = [0, 1, 0]

moveZerores(test1)
moveZerores(test2)
moveZerores(test3)

print(test1)
print(test2)
print(test3)
