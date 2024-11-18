# https://leetcode.com/problems/minimum-knight-moves/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

# Graph

from typing import List
from collections import deque

# Brute force. Times out.
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque()
        visited = set()

        # BFS
        q.append(((0, 0), 0))

        while q:
            position, moves = q.popleft()
            visited.add(position)
            print(position)

            if position[0] == x and position[1] == y:
                return moves

            for move in [[-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1]]:
                new_position = (move[0] + position[0], move[1] + position[1])

                if new_position not in visited:
                    q.append((new_position, moves + 1))

# Bi-directional search
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # the offsets in the eight directions
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        # data structures needed to move from the origin point
        origin_queue = deque([(0, 0, 0)])
        origin_distance = {(0, 0): 0}

        # data structures needed to move from the target point
        target_queue = deque([(x, y, 0)])
        target_distance = {(x, y): 0}

        while True:
            # check if we reach the circle of target
            origin_x, origin_y, origin_steps = origin_queue.popleft()
            if (origin_x, origin_y) in target_distance:
                return origin_steps + target_distance[(origin_x, origin_y)]

            # check if we reach the circle of origin
            target_x, target_y, target_steps = target_queue.popleft()
            if (target_x, target_y) in origin_distance:
                return target_steps + origin_distance[(target_x, target_y)]

            for offset_x, offset_y in offsets:
                # expand the circle of origin
                next_origin_x, next_origin_y = origin_x + offset_x, origin_y + offset_y
                if (next_origin_x, next_origin_y) not in origin_distance:
                    origin_queue.append((next_origin_x, next_origin_y, origin_steps + 1))
                    origin_distance[(next_origin_x, next_origin_y)] = origin_steps + 1

                # expand the circle of target
                next_target_x, next_target_y = target_x + offset_x, target_y + offset_y
                if (next_target_x, next_target_y) not in target_distance:
                    target_queue.append((next_target_x, next_target_y, target_steps + 1))
                    target_distance[(next_target_x, next_target_y)] = target_steps + 1

s = Solution()

assert(s.minKnightMoves(2, 1) == 1)
assert(s.minKnightMoves(5, 5) == 4)
s.minKnightMoves(2, 112)
