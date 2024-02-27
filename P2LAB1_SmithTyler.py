#Tyler Smith
#02/26/2024
#P2LAB1
#this program will ask the user to input values for vehicle MPG and ask for fuel cost
#it will calculate costs for 20/75/500 miles of travel.

while True:
    try:
        mpg = float(input('What is your vehicles average miles per gallon of fuel (MPG?):\n '))
        if mpg <= 0:
            print('... Your car may be in reverse. Please enter a positive number. ')
            raise ValueError
        elif mpg >= 0:
            break
    except ValueError:
        print ('This is not a valid MPG.')

while True:
    try:
        fuelcost = float(input('How much does a gallon of fuel cost you?:\n$ '))
        if fuelcost <= 0:
            print('I wish fuel was so cheap..')
            raise ValueError
        elif fuelcost >= 0:
            break
    except ValueError:
        print ('This is not a valid fuel cost. please enter the current cost of fuel.')

cost_per_mile = (fuelcost * ( 1 / mpg))

print ('\nYour vehicle\'s fuel will cost:')
print (f'${cost_per_mile * 20:.2f}', 'to travel 20 miles...')
print (f'${cost_per_mile * 75:.2f}', 'to travel 75 miles...')
print (f'${cost_per_mile * 500:.2f}', 'to travel 500 miles.')

tripmiles = float(input('\nHow many miles are you driving?:\n '))
print (f'That will cost you ${cost_per_mile * tripmiles:.2f}' ' to travel', tripmiles,'miles.')

print (f'This travel will use {tripmiles / mpg:.2f}', 'gallons of fuel.')

entR = input('\nPress enter to exit..')
exit()

