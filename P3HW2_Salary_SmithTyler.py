

#Tyler Smith
#03/24/2024
#P3HW2
#this program calculates an employee's pay based on user inputs (hrs works, pay rate)
#program displays output values containing hrs worked, pay rate, overtime hrs, overtime pay, regular pay, gross pay.


# User will input an employees name
# User inputs employee hours worked this week
# User inputs employee pay rate
#
# If the hours worked is less than 40
# 	regular hours = hours worked this week
# 	overtime hours = 0
#	regular pay = hours worked multiplied by pay rate
# Else: (if hours are > 40)
#	regular hours = 40
#	overtime hours = hours worked - 40
#	overtime pay = 1.5(overtime hours * payrate)
# Gross pay will always = regular pay + overtime pay
#
# prints line break, Employee name info under line break
# prints columns containing: Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay, Gross Pay
# line break
# Prints user hours, formats to print next line without line break
# Prints pay rate, formats to print next line without line break
# Prints OT hours, formats to print next line without line break
# Prints OT pay, formats to print next line without line break
# Prints regular pay, formats to print next line without line break
# Prints gross pay

user_name = input('Enter employee\'s name: ')
user_hours = float(input('Enter number of hours worked: '))
user_rate = float(input('Enter employee\'s pay rate: '))

if user_hours <= 40:
    reg_hrs = user_hours
    ot_hrs = 0
    ot_pay = 0
    reg_pay = (user_hours * user_rate)
else:
    reg_hrs = 40
    ot_hrs = (user_hours - 40)
    ot_pay = (1.5 * (ot_hrs * user_rate))
    reg_pay = (user_rate * 40)
gross_pay = (reg_pay + ot_pay  )

print ('--------------------------------\nEmployee name:',user_name)
print ('Hours Worked     Pay Rate     OverTime    OverTime Pay    RegHour Pay    Gross Pay')
print ('--------------------------------------------------------------------------------------')
print (f'{user_hours:<16.2f}',end = " ")
print (f'{user_rate:<12.2f}',end = " ")
print (f'{ot_hrs:<11.2f}',end = " ")
print (f'{ot_pay:<15.2f}',end = " ")
print (f'${reg_pay:<13.2f}',end = " ")
print (f'${gross_pay}')




