"""
Question: 
Given an unsorted array arr[0..n-1] of size n.
Find the minimum length subarray arr[s..e] such that sorting this subarray makes the whole array sorted. 
Examples: 
1) If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60],
   your program should be able to find that the subarray lies between 
   the indexes 3 and 8.
2) If the input array is [0, 1, 15, 25, 6, 7, 30, 40, 50],
   your program should be able to find that the subarray 
   lies between the indexes 2 and 5.
"""

def minimum_unsorted_subarray(n, arr):
    start_index = -1
    end_index = -1

    #Find first irregularity
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            start_index = i+1
            break
    
    #Find last irregularity
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            end_index = i 
            break       

    #In case of any irregularity
    if start_index != -1 and end_index != -1:
        #Find min and max in between the indices of irregularity
        min_ele = min(arr[start_index:end_index+1])
        max_ele = max(arr[start_index:end_index+1])

        #Find the first greater element than min_ele
        for i in range(start_index):
            if arr[i] > min_ele:
                start_index = i
                break
        
        #Find the first smaller element than max_ele
        for i in range(end_index+1, n):
            if arr[i] < max_ele:
                end_index = i
                break
        
        return (start_index, end_index)
    
    return "List already sorted!"

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    ans = minimum_unsorted_subarray(n, arr)
    print(ans)
