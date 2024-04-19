#Tyler Smith
#04/18/2024
#P5LAB
#this tool uses a function to determine whether user-input year is a leap year.
#function is called in output to list the number of days in February for given year.
#Alternative solution provided as comment.

def days_in_feb(user_year):
    if (user_input % 400 == 0) or (user_input % 4 == 0) and (user_input % 100 != 0):
        return '29'
    else:
        return '28'

if __name__ == '__main__':
    user_input = int(input('Enter Year: '))
    days_print = days_in_feb(user_input)
print(f'{user_input} has {days_print} days in February')


#ALTERNATIVELY :
#input_year = int(input('Enter Year: '))
#def days_in_feb(user_year):
    #if (input_year % 400 == 0) or (input_year % 4 == 0) and (input_year % 100 != 0):
        #return '29'
    #else:
        #return '28'
#print(f'{input_year} has',days_in_feb(input_year),'in February.')