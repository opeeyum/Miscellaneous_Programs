"""
The problem is to count all the possible paths,
from top left to bottom right of a m X n matrix,
with the constraints that from each cell you can either move to RIGHT or DOWN
"""

def total_path(m:int, n:int) -> int:
    if m == 1 or n == 1:
        return 1
    
    return total_path(m-1, n) + total_path(m, n-1)


print(total_path(3, 3))