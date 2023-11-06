X = float(input('Enter a number: '))
y = float(input('Enter a number: '))
z = float(input('Enter a number: ') #syntax error, parenthesis was never closed

mean = x+y+z/2 #logic error should divide sum of x,y, z not just z by number of values inputted (3) #runtime error name error: x not defined

print"The mean of the two numbers is: " + mean #syntax error, missing parenthesis