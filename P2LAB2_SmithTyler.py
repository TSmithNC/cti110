#Tyler Smith
#02/27/2024
#P2LAB2
#Tool will prompt user to enter 4 numbers. input must be a number not equal to 0
#After providing four numbers, will calculate product and average of all four inputs
#will output product and average values in floating point, and rounded to nearest whole number.

#Number 1
while True:
    try:
        num1 = float(input('Enter first number:'))
        w = num1
        if num1 == 0:
            raise ValueError
        else:
            break
    except ValueError:
        print('Input is not valid')
#Number 2
while True:
    try:
        num2 = float(input('Enter second number:'))
        x = num2
        if num2 == 0:
            raise ValueError
        else:
            break
    except ValueError:
        print('Input is not valid')
#Number 3
while True:
    try:
        num3 = float(input('Enter third number:'))
        y = num3
        if num3 == 0:
            raise ValueError
        else:
            break
    except ValueError:
        print('Input is not valid')
#Number 4
while True:
    try:
        num4 = float(input('Enter fourth number:'))
        z = num4
        if num4 == 0:
            raise ValueError
        else:
            break
    except ValueError:
        print('Input is not valid')

prod = (w * x * y * z)
prod_int = round(prod)
avg = ((w + x + y + z) / 4)
avg_int = int(round(avg))
float_prod = (num1 * num2 * num3 * num4)
print (f'\nProduct of Numbers(rounded): {prod_int:.0f}')
print (f'Average of Numbers(rounded): {avg_int:.0f}')
print (f'\nProduct of Numbers(Floating Point): {float_prod:.3f}')
print (f'Average of Numbers(Floating Point): {avg:.3f}')
