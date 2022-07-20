from typing import List

def two_sum(arr:List[int], target:int ) -> List[int]:
    helper = {}
    for i in range(len(arr)):

        # If element present in helper get its value
        if arr[i] in helper:
            return [helper[arr[i]], i]
        
        # If element not present add the appropiate key value pair
        helper[target-arr[i]] = i


# arr = [3, 5, 8, 2]
# target = 5
# print(*two_sum(arr, target))

		
		
  