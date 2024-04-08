#Tyler Smith
#04/06/24
#P4LAB2
#tool uses (2) integer inputs and determines numbers which are increments of 5 between these numbers.

input1 = int(input('Enter an integer 1: '))
input2 = int(input('Enter an integer 2: '))
output = []

if input1 <= input2:
    for i in range(input1, input2, 5):
        output.append(i)
else:
    print('Second integer can\'t be less than the first.')
if ((input2 - input1) % 5) == 0 and input1 <= input2:
    output.append(input2)
print(*output, '\n' )



