# https://leetcode.com/problems/nested-list-weight-sum/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        multiplier = 1

        def calculate(l: List[NestedInteger], multiplier: int):
            result = 0

            for item in l:
                if item.isInteger():
                    result += item.getInteger() * multiplier
                else:
                    result += calculate(item.getList(), multiplier + 1)
            
            return result

        return calculate(nestedList, multiplier)


# Test cases
# [[1,1], 2, [1, 1]] = 10
# [1, [4, [6]]] = 27
# [0] = 0