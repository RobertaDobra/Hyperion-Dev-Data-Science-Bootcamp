numbers = [input("Enter a floating number: ") for i in range(10)] #for loop allows the user to input exactly 10 times(i.e input then press enter x10, all these inputs will be stored as a list)
float_numbers = [float(value) for value in (numbers)] #converts input into float variable
print("Floating Values List : " + str(float_numbers)) #prints the inputs
import math
sum=sum(float_numbers) #sum is all numbers added together
max=max(float_numbers) #first find the max value
min=min(float_numbers) #finds the min value
indexmax = float_numbers.index(max)
indexmin = float_numbers.index(min)
count=len(float_numbers) #length of the list gives number of elements in the list
average=sum/count #average is all numbers added together divided by the number of elements
rounded_average = round(average, 2) #2 from here is the number of decimal places one requires of the result 'average' 
import statistics
median=statistics.median(float_numbers) #function from the statistics library

print("Sum of numbers entered: " + str(sum))
print("Index of max number: "+ str(indexmax))
print("Index of min number: "+ str(indexmin))
print("Average of numbers entered to 2 d.p: " + str(rounded_average))
print(str(median)) #results print