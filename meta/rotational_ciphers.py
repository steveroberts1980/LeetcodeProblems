import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  ord_a = ord('a')
  ord_A = ord('A')
  cipher = [None]*len(input_str)

  for i in range(len(input_str)):
    # Check if number. If digit, then add rotation_factor and % 9
    if str(input_str[i]).isdigit():
      cipher[i] = str((int(input_str[i]) + rotation_factor) % 10)
    elif ord(input_str[i]) < ord_a + 26 and ord(input_str[i]) >= ord_a:
      # get the offset from a
      cipher[i] = chr(((ord(input_str[i]) - ord_a) + rotation_factor) % 26 + ord_a)
    elif ord(input_str[i]) < ord_A + 26 and ord(input_str[i]) >= ord_A:
      cipher[i] = chr(((ord(input_str[i]) - ord_A) + rotation_factor) % 26 + ord_A)
    else:
      cipher[i] = input_str[i]
  return ''.join(cipher)











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
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  