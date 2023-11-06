input_string=str(input("Enter a text: "))

mydict = {} #currently empty

for character in input_string:
    if character.lower() in mydict:
        mydict[character.lower()] += 1 #this is the syntax of dictionaries that shows key and value, in square brackets we have the key. The value for key increases by 1 with each occurrence of the character in the text input from the user
    else:
        mydict[character.lower()] = 1 #value for key stays the same     

print(mydict) #prints results from for loop after user entered the input