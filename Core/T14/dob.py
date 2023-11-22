f = open('DOB.txt', 'r+') 
file_data="" #create variable to store the following

for line in f:
  file_data = file_data + line

file_data = file_data.split(",") #split data for each person according to the comma from original file

name = []
birthdate = []

for person in range(len(file_data)): #looping through each item in list
  name.append(" ".join(file_data[person].split()[0:2])) #first 2 elements are names; looping for each person then split data according to the white space from list and add element through join function
  birthdate.append(" ".join(file_data[person].split()[-3:])) #last three elements are dates

print ("Name :") 
print ("\n".join(name))

print ("Birthdate :") 
print ("\n".join(birthdate))