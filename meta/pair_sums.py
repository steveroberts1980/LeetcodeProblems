import math
from typing import DefaultDict
# Add any extra import statements you may need here


# Add any helper functions you may need here


def numberOfWays(arr, k):
    # Write your code here
    nums = DefaultDict(list)
    
    # Use a set to keep track of the pairs
    combos = 0

    # Create the hash of numbers and indexes
    for i in range(len(arr)):
        nums[arr[i]].append(i)

    for i in range(len(arr)):
       val = k - arr[i]
       if val in nums:
          combos += len([idx for idx in nums[val] if (idx != i and idx > i)])
    
    return combos

  












# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  

  # Approach

  # Brute force is we can try every combo with 2 pointers.
  # Start with ptr1 at 0 and ptr2 at 2
  # Run ptr2 to the end and then increment ptr1
  # Do this until ptr1 is at len(arr) - 2 position.

  # Runtime will be O(N^2)
  # Space complexity will be O(1)

  # Can it be done in O(N) time? 
  # We could create a dict of the numbers and indexes of those numbers.
  # The hashmap values will need to be a list since the numbers can appear more 
  # than once.

  # Check to ensure the index is not the current index