"""
Given a characters array letters that is sorted in non-decreasing order and a character target,
return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 
Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"

Example 3:
Input: letters = ["c","f","j"], target = "d"
Output: "f"
"""
def nextGreatestLetter(letters, target: str) -> str:
    start = 0
    end = len(letters)-1
    while start <= end:
        mid = (start+end) // 2
        if ord(letters[mid]) > ord(target):
            end = mid-1
        else:
            start = mid +1
    return letters[start%len(letters)]

test1 = ["c","f","j"]
target1 = "a"
target2 = "c"
target3 = "d" 
print(nextGreatestLetter(test1, target1))
print(nextGreatestLetter(test1, target2))
print(nextGreatestLetter(test1, target3))       