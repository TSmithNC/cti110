#Tyler Smith
#03/04/24
#P2HW2
#user inputs (test grades) are added to a list.
#List is used to calculate Min/Max/Sum of grades/Avg grade.

#Psuedocode:
    #Create an empty list for module grades. user input will append into list.

    #Print descriptive header for tool
    #assign mod1 input as variable for Module 1 grade
    #Append "modulegrades" list to add mod1 floating point value
    #assign mod2 input as variable for Module 2 grade
    #Append "modulegrades" list to add mod2 floating point value
    #assign mod3 input as variable for Module 3 grade
    #Append "modulegrades" list to add mod3 floating point value
    #assign mod4 input as variable for Module 4 grade
    #Append "modulegrades" list to add mod4 floating point value
    #assign mod5 input as variable for Module 5 grade
    #Append "modulegrades" list to add mod5 floating point value
    #assign mod6 input as variable for Module 6 grade
    #Append "modulegrades" list to add mod6 floating point value

    #print "results" with "------"line break
    #print "lowest grade:"  +  minimum grade using MIN sequence type function on "modulegrades" list
    #print "Highest grade:" +  maximum grade using MAX sequence type function on "modulegrades" list
    #print "Sum of Grades:" +  sum total of list inputs using SUM sequence type function on "modulegrades" list
    #print "Average:"       +  (.##) average grade using SUM/LENGTH sequence type operation on "modulegrades" list
    #print "-------------" line break

modulegrades = []

print ('Enter Test grades for each module\n-----------------------------------')
mod1 = float(input('Enter Grade for Module 1: '))
modulegrades.append(mod1)
mod2 = float(input('Enter Grade for Module 2: '))
modulegrades.append(mod2)
mod3 = float(input('Enter Grade for Module 3: '))
modulegrades.append(mod3)
mod4 = float(input('Enter Grade for Module 4: '))
modulegrades.append(mod4)
mod5 = float(input('Enter Grade for Module 5: '))
modulegrades.append(mod5)
mod6 = float(input('Enter Grade for Module 6: '))
modulegrades.append(mod6)

print ('\n------------Results------------')
print (f'Lowest Grade:       {min(modulegrades)}')
print (f'Highest Grade:      {max(modulegrades)}')
print (f'Sum of Grades:      {sum(modulegrades)}')
print (f'Average:            {sum(modulegrades) / len(modulegrades):.2f}')
print ('-------------------------------')
