import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def substring_chars(sub: dict):
    sum = 0
    for k in sub:
       sum += sub[k]

    return sum

def min_length_substring(s, t):
    # Write your code here
    sub_chars = {}

    if len(t) > len(s):
        raise Exception("String t is shorter than s")
  
    # build dict of chars in t
    for char in t:
        sub_chars[char] = sub_chars.get(char, 0) + 1

    # now see if the string has all the characters of the substring
    for char in s:
       if char in sub_chars:
        sub_chars[char] -= 1

    for k in sub_chars:
       if sub_chars[k] > 0:
          return -1

    left, right = 0, len(s) - 1

    while s[right] not in sub_chars or s[left] not in sub_chars and substring_chars(sub_chars) < 0:
        # try removing the character at left. If it is still a substring, then keep trying left until it is not a substring
        if s[left] in sub_chars:
            sub_chars[s[left]] += 1
            if substring_chars(sub_chars) <= 0:
                left += 1
            else:
               sub_chars[s[left]] -= 1
        else: # It is not even a substring character
            left += 1

        if s[right] in sub_chars:
            sub_chars[s[right]] += 1
            if substring_chars(sub_chars) <= 0:
                right -= 1
            else:
                sub_chars[s[right]] -= 1
        else:
           right -= 1

    return right - left + 1
       
  











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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  


  # Approach
  # We can use 2 pointers. A right and left pointer. 
  # Then we can move both pointers until we get a match on 
  # one of the characters. Then, continue moving until we have 
  # matched all the characters required. Once we have all the characters 
  # included, note down the substring length. 
  # Continue to the end of the string. If we get another substring that is shorter
  # update the minimum substring length.

  # To keep track of whether we have captured all the characters,
  # use a list or hash table. 

  # "fd"

  # l = 0, r = 