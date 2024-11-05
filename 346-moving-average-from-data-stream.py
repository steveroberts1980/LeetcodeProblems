# https://leetcode.com/problems/moving-average-from-data-stream/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=EASY&role=full-stack&status=TO_DO%2CATTEMPTED

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.ptr = 0
        self.arr = [0]*size
        self.cnt = 0
        self.sum = 0
        

    def next(self, val: int) -> float:
        self.sum -= self.arr[self.ptr]
        self.arr[self.ptr] = val
        self.sum += val

        self.ptr = (self.ptr + 1) % self.size

        self.cnt += 1
        return self.sum / min(self.cnt, self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
s = MovingAverage(3)
print(s.next(1))
print(s.next(10))
print(s.next(3))
print(s.next(5))