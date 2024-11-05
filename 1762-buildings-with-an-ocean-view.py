# https://leetcode.com/problems/buildings-with-an-ocean-view/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Intuitive method: start at the end of the list. 
        # Keep a counter of the current max building height.
        # When we get a building with a new max, update and add that index 
        # to the front of our list
        # In order to prevent re-creating the list each time,
        # we can just append and then reverse the list to return

        # the first max will always be the last building.
        max = 0
        with_views = list()

        num_buildings = len(heights)

        for i in range(num_buildings):
            indx = num_buildings - 1 - i
            if heights[indx] > max:
                with_views.append(indx)
                max = heights[indx]
        
        with_views.reverse()
        return with_views


s = Solution()

assert(s.findBuildings([4,2,3,1]) == [0,2,3])
assert(s.findBuildings([4,3,2,1]) == [0,1,2,3])
assert(s.findBuildings([1,3,2,4]) == [3])

