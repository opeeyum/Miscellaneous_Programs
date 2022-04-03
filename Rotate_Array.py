"""
Question: Given an array, rotate the array to the right by k steps, where k is non-negative.

Could you do it in-place with O(1) extra space?

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
def rotate(nums, k:int) -> None:
    x, y, break_Up_point= 0, len(nums)-k-1, len(nums)-k 
    while x != 0 or y != 0:
        if x > y:
            for _ in range(k):
                nums[x], nums[y] = nums[y], nums[x]
                x += 1
                y += 1
            #Incompelete

        elif x < y:
            pass
        else:
            # x == y
            pass

test1 = [1, 2, 3, 4, 5, 6, 7]
test2 = [-1, -100, 3, 99]

rotate(test1)
rotate(test2)

print(test1)
print(test2)