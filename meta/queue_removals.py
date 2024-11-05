import math
from collections import deque
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findPositions(arr, x):
    # Write your code here
    q = deque()
    tmp_q = deque()
    max_val = None
    ret_val = [None] * x

    # populate the queue from the array
    for i in range(len(arr)):
      q.append((arr[i], i+1)) # push the value and the original index onto the queue
  
    for iteration in range(x):
        max_val = None
        for _ in range(x):
            # pop x elements from the queue. If fewer than x remain, pop until empty
            # when popping, keep track of the largest
            # can keep the current element and if the next is larger, then 

            # keep a second queue that we pop back onto the first from
            # keep a reference to the max value and when adding back to the 
            # original queue, skip it
            if len(q) == 0:
                break

            tmp = q.popleft()
            if not max_val: # keep track of the max
                max_val = tmp
            elif tmp[0] > max_val[0]:
                max_val = tmp
            
            tmp_q.append(tmp) # pop off the queue

        # now we should have the max value
        # add it to the return
        ret_val[iteration] = max_val[1]
            
        # now add the items from the tmp_q back to the end of the q
        # decrement as they are added
        while tmp_q:
            tmp = tmp_q.popleft()

            if tmp != max_val:
                tmp = (max(0, (tmp[0]-1)), tmp[1])
            
                q.append(tmp)
  
    return ret_val









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 6
  x_1 = 5
  arr_1 = [1, 2, 2, 3, 4, 5]
  expected_1 = [5, 6, 4, 1, 2]
  output_1 = findPositions(arr_1, x_1)
  check(expected_1, output_1)

  n_2 = 13
  x_2 = 4
  arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
  expected_2 = [2, 5, 10, 13]
  output_2 = findPositions(arr_2, x_2)
  check(expected_2, output_2)

  # Add your own test cases here
  