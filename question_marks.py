# Have the function question_marks(stri) take the stri string parameter, which will contain 
# single digit numbers, letters, and question marks, and check if there are exactly 3 question marks 
# between every pair of two numbers that add up to 10. 

# If so, then your function should return True, otherwise it should return False. 
# If there aren't any two numbers that add up to 10 in the string, then your function should return false as well.

# For example: if stri is "arrb6???4xxbl5???eee5" then your function should return True because there are 
# exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

# Input: "aa6?9"          Input: "acc?7??sss?3rr1??????5"
# Output: False           Output: True

# Test your function with the test cases below!

def question_marks(stri):
    str_numbers = '0123456789'
    # Create a string of all possible integers to check for numbers
    num_questions = 0
    # Variable to store the number of question marks between numbers
    save_int = 0
    # Since we're going to iterate up through the string
    # Create a variable that will store the previous number in the string
    # so we can check if two numbers will add up to 10
    three_q_and_10 = False
    # Create a variable to record a boolean value for the case of numbers
    # adding up to 10 
    for character in stri:
        # Iterate throug the initial string and set variable 'character'
        # for each character in the string
        if character in str_numbers:
            # If the character is a number
            if int(character) + save_int == 10:
                # FIRST CHECK: If the number value of the character + save_int 
                # (save_int is 0 to start - so we'll skip the first round) 
                # is equal to 10 - case we're looking for
                print(f'{save_int} + {character} = 10')
                if num_questions == 3:
                    print(f'Question Marks: {"?" * num_questions} ✅')
                elif num_questions != 3:
                    print(f'Question Marks: {"?" * num_questions} ❌')
                    # SECOND CHECK: If the number of question marks we have stored
                    # for characters between these two numbers is NOT EQUAL to 3
                    # return False, even if the numbers add up to 10
                    return False
                # Otherwise, since the two numbers add up to to 10
                # AND there are 3 question marks, three_q_and_10 - our boolean variable
                # for BOTH cases is now set to True
                three_q_and_10 = True
            save_int = int(character)
            # Inside the for in loop, since we're iterating up through each element
            # If we hit a number, save the value of the number as the value of save_int
            # save_int will change every time we hit a number in the iteration
            num_questions = 0
            # After a number is hit, reset the value of the number of questions to 0
            # since we need to check for 3 question marks between EVERY two numbers that add up to 10
        elif character == '?':
        # Inside the for in loop, for every question mark we hit
        # ADD one to the number of question marks 
        # This value will be reset each time we hit a number
            num_questions += 1
    return True if three_q_and_10 else False
    # return True if there are numbers that add up to 10 and all numbers that add up to 10 have 3 question marks 
    # otherwise return False

print(question_marks('aa6?9'))
# should return False

print(question_marks('acc?7??sss?3rr1??????5'))
# should return True

print(question_marks('arrb6???4xxbl5???eee5'))
# should return True

print(question_marks('fal291?se4?rep?u?6kd5??2g9??asdg?1'))
# should return False

print(question_marks('fal21?se4?rep?u?6kd5??2g9??asdg?1al'))
# should return True

print(question_marks('5??aaaaaaaaaaaaaaaaaaa?5?5'))
# should return False

print(question_marks('9???1???9???1???9'))
# should return True
