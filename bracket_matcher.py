# Write a Python function that takes a string input. This string represents code. 
# It may have any number of characters in it, and the characters may be anything. 
# For our purposes, we'll ignore anything that isn't one of the following: [, ], {, }, (, ). 
# Your function definition looks like this:

# def bracket_matcher(input):
# The return value is a boolean. You should return True if the brackets are properly matched and nested, 
# otherwise False.

# Test Cases:
# Think you got it figured out? Run through the test cases below to make sure!


def bracket_matcher(stri):
  # Use a list to define the empty stack
  stack = []
  # Loop over the string and check for opening brackets
  for i in stri:
    if i in ['(', '{', '[']:
      # Push opening brackets to the stack
      stack.append(i)
      print(stack)
    elif i in [')', '}', ']']:
      # Find closing brackets
      if len(stack) == 0:
        # If there are closing brackets and no opening brackets, return false
        return False
      elif len(stack) > 0 and i in [')', '}', ']']:
        # If there are opening brackets, check for a match, then pop the matching opening bracket
        if i == ')' and stack[-1] == '(' or i == '}' and stack[-1] == '{' or i == ']' and stack[-1] == '[':
          print(i)
          print(stack[-1])
          stack.pop()
          print(stack)     
  if len(stack) == 0:
    # Stack will be zero if brackets match
    return True
  else:
    # Brackets do not match if the length of the stack is not zero
    return False


print(bracket_matcher('abc(123)'))
# returns True

print(bracket_matcher('a[b]c(123'))
# returns False -- missing closing parens

print(bracket_matcher('a[bc(123)]'))
# returns True

print(bracket_matcher('a[bc(12]3)'))
# returns False -- improperly nested

print(bracket_matcher('a{b}{c(1[2]3)}'))
# returns True

print(bracket_matcher('a{b}{c(1}[2]3)'))
# returns False -- improperly nested

print(bracket_matcher('()'))
# returns True

print(bracket_matcher('[]]'))
# returns False - no opening bracket to correspond with last character

print(bracket_matcher('abc123yay'))
# returns True -- no brackets = correctly matched