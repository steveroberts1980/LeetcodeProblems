import math
import sys
# Add any extra import statements you may need here


# Add any helper functions you may need here


# def getBillionUsersDay(growthRates):
#   # Write your code here
#   total = 0.0
#   days = 0
  
#   while total < 1000000000.0:
#     total = 0
#     days += 1
#     for r in growthRates:
#       total += math.pow(r, days)
      
#   return days

def getBillionUsersDay(growthRates):
    left, right = 1, 2000
    days = sys.maxsize

    while left <= right:
        mid = (left + right) // 2

        total = 0
        for r in growthRates:
            total += math.pow(r, mid)

        if total == 1000000000.0:
           return mid
        elif total > 1000000000.0:
           days = min(mid, days)
           right = mid - 1
        else:
           left = mid + 1

    return days












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
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  