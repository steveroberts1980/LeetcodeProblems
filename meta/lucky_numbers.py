from typing import List
import sys

def getLuckyNumbers(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    
    row_mins = [sys.maxsize]*len(matrix)
    col_maxs = [sys.maxsize * -1]*len(matrix[0])

    min_vals = set()
    max_vals = set()
    retVal = []

    for row_num in range(0, len(matrix)):
        for col_num in range(0, len(matrix[0])):
            row_mins[row_num] = min(row_mins[row_num], matrix[row_num][col_num])
            col_maxs[col_num] = max(col_maxs[col_num], matrix[row_num][col_num])
    
    for i in row_mins:
        min_vals.add(i)

    for i in col_maxs:
        max_vals.add(i)

    lucky_nums = min_vals.intersection(max_vals)

    for i in range(len(lucky_nums)):
        retVal.append(lucky_nums.pop())

    return retVal

assert(getLuckyNumbers([[3,7,8],[9,11,13],[15,16,17]]) == [15])


####################################
#
#     0   1   2 
# 0   3,  7,  8 
# 1   9, 11, 13  
# 2  15, 16, 17
#
#
####################################
