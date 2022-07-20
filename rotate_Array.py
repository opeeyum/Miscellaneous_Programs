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


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end - 1] = arr[end - 1], arr[start]
        start += 1
        end -= 1


def rotate(arr, k: int) -> None:
    reverse(arr, 0, k)
    reverse(arr, k, len(arr))
    reverse(arr, 0, len(arr))


test1 = [1, 2, 3, 4, 5, 6, 7]
test2 = [-1, -100, 3, 99]

rotate(test1, 3)
rotate(test2, 2)

print(test1)
print(test2)
