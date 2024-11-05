import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def isBalanced(s):
    # Write your code here
  
    # Using a stack, when we come across '(, { or [' then we will push to the stack
    # When we come across the opposite, pop from the stack
    # Check if the popped character is correct. If not, return False
    # When we are done, return True if the stack is empty.
    # Otherwise return False

    stack = list()

    for i in s:
        if i in ['(', '{', '[']:
            stack.append(i)
        else:
           if len(stack) == 0:
              return False
           else:
              tmp = stack.pop()
              if (i == ')' and tmp != '(') or (i == '}' and tmp != '{') or (i == ']' and tmp != '['):
                 return False

    return True










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "{[(])}"
  expected_1 = False
  output_1 = isBalanced(s1)
  check(expected_1, output_1)

  s2 = "{{[[(())]]}}"
  expected_2 = True
  output_2 = isBalanced(s2)
  check(expected_2, output_2)

  # Add your own test cases here
  