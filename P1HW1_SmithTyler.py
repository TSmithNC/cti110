#Tyler Smith
#02/20/2024
#P1HW1
#Will use an input function to determine an integer, Squared value of an Integer, and Cubed value.
#will use initial input along with a secondary input to determine the sum and product of input values.  
import time
print('This tool will help you find a whole number\'s value when squared and cubed.')
input1 = int(input('Enter an whole number:'))
print ('You entered:',input1,)
print ('Calculating! ',end=''),time.sleep(1.5),print(' .',end=''),time.sleep(.75),\
print (' .',end=''),time.sleep(.75),print(' .\n'),time.sleep(1)
print (input1 ,'squared equals:',input1**2),time.sleep(1)
print (input1 ,'cubed equals:',input1**3,('\n'))

print ('Let\'s see what we get if we add and multiply a number to',input1)
input2 = int(input('Select a number:'))
print ('OK! Calculating! ',end=''),time.sleep(1.5),print(' .',end=''),time.sleep(.75),\
print (' .',end=''),time.sleep(.75),print(' .\n'),time.sleep(1)
print (input1,'+',input2,'equals:',input1+input2)
print (input1,'*',input2,'equals:',input1*input2)
print ('Goodbye!')

