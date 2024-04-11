# Tyler Smith
# 04/10/2024
# P4HW1

# This tool asks the user how many scores will be graded. valid scores range 0-100. if input is invalid, user must enter
# A valid input to continue to the next input.

# After input is checked for validity, it is stored in a list to be used later.
# upon completion of input, "results" summary is output. the lowest score is listed, then dropped from the list.
# The modified list is shown, as well as the modified average score, and a letter grade.

#PSUEDOCODE
# Enter the number of grades youd like to use as input
# Variable “scorenum” used in for loop for text “enter score #X”
# Scorelist created empty, to be appended as values are input for ‘score x’


# For loop begins, will repeat for # of grades that were previously entered.
#   ‘Score’  value is input. Score number ‘x’ changes with variable ‘scorenum’.
#   IF ‘score’ value must be between 0 – 100:
#       Scorelist is updated with the provided input
#       ‘Scorenum’ variable increased for next iteration of loop. (‘enter score # x’)
#   IF  ‘score’  is not valid input:
#       While loop begins
#           Print error message.
#           Attempt new input for ‘score’ variable
#           IF score is valid ..
#               Scorelist is updated with the provided input
#               ‘Scorenum’ variable increased for next iteration of loop.

# Prints ‘results’ footer
# Prints lowest grade, to be removed from ‘scorelist’ later.
# Lowest grade removed from ‘scorelist’
# Avg grade variable created, after lowest grade removed from 'scorelist’
# Prints modified list of scores
# Prints modified average grade of scores
# IF: score is greater or equal to 90:
#   Print ‘grade: A’
# IF: score is 80-90:
#   Print ‘grade: B’
# IF: score is 70-80:
#   Print ‘grade: C’
# IF: score is 60-70:
#   Print ‘grade: D’
# IF: score is lower than 60:
#   Print ‘grade: F’
# Print ‘------’ line break

input1 = (int(input('How many scores do you want to enter?: ')))
scorenum = 1
scorelist = []


for i in range(input1):
    score = float(input('Enter score #{}:'.format(scorenum)))
    if score >= 0 and score <= 100:
        scorelist.append(score)
        scorenum = (scorenum + 1)
    else:
        while score <0 or score >100:
            print ('INVALID Score Entered!!!\nScore should be between 0 and 100')
            score = float(input('Enter score #{} again:'.format(scorenum)))
            if score >= 0 and score <= 100:
                scorelist.append(score)
                scorenum = (scorenum + 1)


print ('\n------------Results------------')
print (f'Lowest Grade   : {min(scorelist)}')
scorelist.remove(min(scorelist))
Scoreavg = sum(scorelist) / len(scorelist)
print (f'Modified Scores:{(scorelist)}')
print (f'Scores Average : {(Scoreavg):.2f}')
if Scoreavg >= 90:
    print ('Grade          : A')
elif Scoreavg >= 80 and Scoreavg < 90:
    print ('Grade          : B')
elif Scoreavg >=70 and Scoreavg < 80:
    print ('Grade          : C')
elif Scoreavg >= 60 and Scoreavg < 70:
    print ('Grade          : D')
else:
    print('Grade          : F')
print ('-------------------------------')