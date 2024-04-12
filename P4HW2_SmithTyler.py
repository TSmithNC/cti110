#Tyler Smith
#04/12/2024
#P4HW2
#this tool uses input to gather employee names, hours worked, and pay rate.
#information gathered is used to display the employees overtime hours/overtime pay/regular pay/gross pay
#when user types "Done", summary is diplayed showing # of employees entered/total OT pay/Regular Hour pay/Gross



user_name = ''
employnum = 0
otsum = []
regsum = []
grosssum = []

while user_name != 'Done' or user_name != 'done':
    user_name = input('Enter employee\'s name or \"Done\" to terminate: ')
    if user_name == 'done' or user_name == 'Done':
        break
    else:
        if user_name != 'done' or 'Done':
            employnum = (employnum + 1)
            user_hours = float(input('How many hours did {} work? '.format(user_name)))
            user_rate = float(input('What is {}\'s pay rate:      '.format(user_name)))

            if user_hours <= 40:
                reg_hrs = user_hours
                ot_hrs = 0
                ot_pay = 0
                reg_pay = (user_hours * user_rate)
                regsum.append(reg_pay)
            else:
                reg_hrs = 40
                ot_hrs = (user_hours - 40)
                ot_pay = (1.5 * (ot_hrs * user_rate))
                otsum.append(ot_pay)
                reg_pay = (user_rate * 40)
                regsum.append(reg_pay)
            gross_pay = (reg_pay + ot_pay)
            grosssum.append(gross_pay)

            print('\nEmployee name:', user_name)
            print('\nHours Worked     Pay Rate     OverTime    OverTime Pay    RegHour Pay    Gross Pay')
            print('--------------------------------------------------------------------------------------')
            print(f'{user_hours:<16.2f}', end=" ")
            print(f'{user_rate:<12.2f}', end=" ")
            print(f'{ot_hrs:<11.2f}', end=" ")
            print(f'{ot_pay:<15.2f}', end=" ")
            print(f'${reg_pay:<13.2f}', end=" ")
            print(f'${gross_pay}\n')

print ('\nTotal number of employees entered   : {}'.format(employnum))
print (f'Total amount paid for overtime      : ${(sum(otsum)):.2f}')
print (f'Total amount paid for regular hours : ${(sum(regsum)):.2f}')
print (f'Total amount paid in gross          : ${(sum(grosssum)):.2f}')

#PSUEDOCODE
# user_name is created as empty variable
# "employee number" variable is created to count employees as input is later provided
# "OverTime sum List" created empty, to be appended as input is provided
# "regular pay sum" List created empty, to be appended as input is provided
# "Gross pay sum" List created empty, to be appended as input is provided

# While "username" input is not "Done" or "done"
#    input employee name(user_name), or "Done" to terminate
#    IF username IS "done"
#        terminates while loop
#    ELSE
#        IF username is not "Done" or "done":
#            add 1 to the employee number variable
#            user inputs employee hours
#            user inputs employee pay rate

#            IF: hours are less than 40:
#                all hours are regular hours. employee's hours equals regular hours.
#                Overtime hours = 0
#                Overtime pay = 0
#                regular pay = hours worked * pay rate
#            Else(over 40 hours worked):
#                regular hours = 40
#                Overtime hours = hours worked - 40
#                OverTime pay = 1.5(overtime hours*pay rate)
#                "Overtime sum" list appended with employee's OT pay value
#                regular pay = user pay rate * 40 hours
#                "Regular pay sum" list appended with employee's regular pay value
#            Gross pay = regular pay + overtime pay
#            "gross pay sum" list appended with employee's gross pay value
#
#            Prints employee name
#            Prints "hours worked, pay rate, overtime, overtime pay, regular pay, gross pay"
#            prints line break "-----"
#             Prints user hours, formats to print next line without line break
#             Prints pay rate, formats to print next line without line break
#             Prints OT hours, formats to print next line without line break
#             Prints OT pay, formats to print next line without line break
#             Prints regular pay, formats to print next line without line break
#             Prints gross pay

# prints number of employees that were input.
# prints dollar value paid for all employee overtime
# prints dollar value paid for all employee regular hours
# prints dollar value paid for all employee gross pay
