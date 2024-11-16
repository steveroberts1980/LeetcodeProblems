# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

import random

class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.data_list = list()

    def insert(self, val: int) -> bool:
        # Save the item in the data hash for quick retrieval
        # Save the item in the list for quick removal
        if val in self.data:
            return False

        self.data[val] = len(self.data_list) # This will be the index the item is place in        
        self.data_list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val in self.data:
            # First, we need to move the item to the end of the list.
            # Then we can pop it in O(1) time
            idx = self.data[val]

            swap_val = self.data_list[-1] # Get the value of the last item. This item index needs to be updated in the hash
            self.data[swap_val] = idx
            self.data_list[-1] = val
            self.data_list[idx] = swap_val
            self.data_list.pop()
            del self.data[val]
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.data_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()