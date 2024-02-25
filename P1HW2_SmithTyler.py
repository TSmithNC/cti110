#Tyler Smith
#02/20/2024
#P1HW1
#this program will asistance in creating a budget for your travel by using inputs to calculate your expenses
#Initial budget, fuel, hotel cost and accomodations, and food cost will be considered.
#this program will then output a value in dollars of estimated expenses and available budget after expenses


print ('Use this tool to help calculate your expenses')
#BUDGET
while True:
     try:
         budget1 = float(input('Enter Budget: $'))
#TRAVEL LOCATION
         dest = input('Enter your travel location: ')
         break
     except ValueError:
         print ('Please enter valid input.... Example:$1.23')
     else:
        budget1 = float(input('Enter Budget: $'))
DestCap = str.title(dest)
#FUEL
while True:
     try:
        fuel = float(input('How much do you think you will spend on gas?: $'))
        break
     except ValueError:
        print ('Please enter valid input.... \nExamples : $40.56, $40')
     else:
         break
#accomodations
while True:
     try:
         accom = float(input('How much do you will need for accomodations/hotel?: $'))
         break
     except ValueError:
         print ('Please enter valid input.... \nExamples : $x.xx or $12.34')
     else:
         break
#FOOD
while True:
    try:
        food = float(input('How much will you need for food?: $'))
        break
    except ValueError:
        print ('Please enter valid input.... \nExamples : $x.xx or $12.34')
    else:
        break


print ('\n')
print ('------------Travel Expenses------------\nLocation:',DestCap)
print ('Initial Budget:$', format(budget1, ",.2f"))
print ('\nFuel cost estimate:$', format(fuel, ",.2f"))
print ('Accomodations:$', format(accom, ",.2f"))
print ('Food:$', format(food, ",.2f"))
print ('\nTotal Expenses:$', format(fuel + accom + food, ",.2f"))
print ('Remaining Balance:$', format(budget1 - fuel - accom - food, ",.2f"))

entR = input('\nPress enter to exit..')
exit()
