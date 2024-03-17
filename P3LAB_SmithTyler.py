#Tyler Smith
#03/17/24
#P3HW1
#user inputs (test grades) are added to a list.
#List is used to calculate Min/Max/Sum of grades/Avg grade.

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum_grades = sum(grades)
avg_grades = (sum_grades / len(grades))

# determine letter grade for average

print ('\n------------Results------------')
print ('Lowest Grade:       ',low)
print ('Highest Grade:      ',high)
print ('Sum of Grades:      ',sum_grades)
print (f'Average:             {avg_grades:.2f}')
print ('-------------------------------')
if avg_grades >= 90:
 print ('Your grade is: A')
elif avg_grades >= 80 and avg_grades < 90:
  print ('Your grade is: B')
elif avg_grades >= 70 and avg_grades < 80:
  print ('Your grade is: C')
elif avg_grades >= 60 and avg_grades < 70:
  print ('Your grade is: D')
else:
    print ('Your grade is: F')
