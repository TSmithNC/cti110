#Tyler Smith
#04/24/2024
#P5HW
# this program produces two random numbers, which the user can use to test basic math skills.
# program keeps count of attempts to correctly answer math problem. attempts reset after correct answer provided.
# program only ends if user inputs "3" from main menu.
import random

print ('MAIN MENU\n__________________')
print ('1: Adding Random Numbers\n2: Subtracting Random Numbers\n3: Exit\n')
menu_input = 0

while menu_input != 3:
    while menu_input == 0:
        try:
            menu_input = (int(input('Please choose one of the menu options:')))
        except ValueError:
            print('Not a Valid Option..')
            break
        if menu_input == 1 or menu_input == 2 or menu_input == 3:
            break
        while menu_input != 1 or menu_input != 2 or menu_input != 3:
            print('Please enter a valid menu option.')
            print('MAIN MENU\n__________________')
            print('1: Adding Random Numbers\n2: Subtracting Random Numbers\n3: Exit\n')
            menu_input = (int(input('Please choose one of the menu options:')))
            if menu_input >= 1 and menu_input <= 3:
               break
#option1(addition)
    attemptcount = 0
    while menu_input == 1 and menu_input !=3:
        while menu_input == 1:
            int1 = random.randint(1, 10)
            int2 = random.randint(1, 10)
            answer = (int1 + int2)
            print (int1,'+', int2 )
            while menu_input == 1:
                attempt = (int(input('Enter Answer:')))
                attemptcount = (attemptcount + 1)
                if attempt == answer:
                    print ('Congratulations!!!! Your answer is correct.')
                    print ('Number of guesses: ',attemptcount)
                    print('MAIN MENU\n__________________')
                    print('1: Adding Random Numbers\n2: Subtracting Random Numbers\n3: Exit\n')
                    menu_input = 0
                    attemptcount = 0
                else:
                    if attempt < answer:
                        print ('Sorry, guess is too low.\nTry again:')
                    if attempt > answer:
                        print ('Sorry, guess is too high.\nTry again:')
#option2(subtraction)
    attemptcount = 0
    while menu_input == 2 and menu_input !=3:
        while menu_input == 2:
            int1 = random.randint(1, 10)
            int2 = random.randint(1, 10)
            answer = (int1 - int2)
            print (int1,'-', int2 )
            while menu_input == 2:
                attempt = (int(input('Enter Answer:')))
                attemptcount = (attemptcount + 1)
                if attempt == answer:
                    print ('Congratulations!!!! Your answer is correct.')
                    print ('Number of guesses: ',attemptcount,'\n__________________')
                    print('MAIN MENU\n__________________')
                    print('1: Adding Random Numbers\n2: Subtracting Random Numbers\n3: Exit\n')
                    menu_input = 0
                    attemptcount = 0
                else:
                    if attempt < answer:
                        print ('Sorry, guess is too low.\nTry again:')
                    if attempt > answer:
                        print ('Sorry, guess is too high.\nTry again:')
print ('Thank you for playing...\nBye!!')








