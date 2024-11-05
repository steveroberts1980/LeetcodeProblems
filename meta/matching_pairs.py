import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
    # Write your code here
    if len(s) < 2:
        return -1
    
    if len(s) == 2:
        if s[0] == t[1] or s[1] == t[0]:
            if s[0] == t[1] and s[1] == t[0]:
                return 2
            return 1
        return 0
    
    offset = ord('a')
  
    # Create arrays to keep track of character counts
    s_mismatches = [0]*26
    t_mismatches = [0]*26
    matches = [0]*26
    pairs = 0

    for i in range(len(s)):
        if s[i] != t[i]:
            s_mismatches[ord(s[i]) - offset] += 1
            t_mismatches[ord(t[i]) - offset] += 1
        else:
            matches[ord(s[i]) - offset] += 1
            pairs += 1

    if pairs == len(s): # All the characters matches
       # Now check to see if there are 2 of the same character in the matches.
       for i in range(len(matches)):
          if matches[i] > 1: # There were 2 of the same character in the string. We can swap those and the strings still all match
             return len(s)
          else:
             return len(s) -2 # We had to swap 2 characters that previously matched but now don't.
    else: # Not all characters matched
        # Now loop through the mismatches to see what we can swap. If we have 1 of the same characters, we can at least swap that. 
        # If 2, then we can swap both and return pairs + 2
        char_matches = 0
        for i in range(len(s_mismatches)):
            if s_mismatches[i] > 0 and t_mismatches[i] > 0:
                char_matches += 1

        return pairs + char_matches
    
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
    # s_1, t_1 = "abcde", "adcbe"
    # expected_1 = 5
    # output_1 = matching_pairs(s_1, t_1)
    # check(expected_1, output_1)

    # s_2, t_2 = "abcd", "abcd"
    # expected_2 = 2
    # output_2 = matching_pairs(s_2, t_2)
    # check(expected_2, output_2)

    # assert matching_pairs('abcd', 'abcd') == 2
    # assert matching_pairs('abcde', 'adcbe') == 5

    # assert matching_pairs('aa', 'aa') == 2
    # assert matching_pairs('aa', 'bb') == 0

    # assert matching_pairs('at', 'at') == 0
    # assert matching_pairs('at', 'ta') == 2
    # assert matching_pairs('ax', 'ya') == 1

    # assert matching_pairs('ax', 'aa') == 1
    # assert matching_pairs('aa', 'ax') == 1

    # assert matching_pairs('abx', 'abb') == 2
    # assert matching_pairs('abb', 'axb') == 2

    # assert matching_pairs('ax', 'ay') == 0
    assert matching_pairs('axb', 'ayb') == 1

    assert matching_pairs('ABC', 'ADB') == 2
    assert matching_pairs('abcde', 'axcbe') == 4
    assert matching_pairs('docomo', 'docomo') == 6

    assert matching_pairs('abcdc', 'baccd') == 3
    assert matching_pairs('abcdx', 'abxcc') == 4

    assert matching_pairs('abcd', 'adcb') == 4
    assert matching_pairs('mno', 'mno') == 1
    assert matching_pairs('abcde', 'adcbe') == 5

    assert matching_pairs('abcd', 'abcd') == 2
    assert matching_pairs('abcd', 'efgh') == 0
    assert matching_pairs('abcd', 'abce') == 2
    assert matching_pairs('abczz', 'abcee') == 3
    assert matching_pairs('abc', 'abd') == 1
    assert matching_pairs('mnode', 'mnoef') == 4

    assert matching_pairs('abxce', 'abcdx') == 3
    assert matching_pairs('dd', 'dd') == 2

    print("All tests passed!")

  # Add your own test cases here
  