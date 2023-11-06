name = input("Please enter a name, enter John to end the task: ")
name_list = []
while name != "John":
    name_list.append(name)
    name = input("Please enter a name: ")
print(name_list)

#I cannot figure out how to eliminate case sensitivity with lower() or upper() when entering 'john' or 'John' or 'joHn' or other alternating cases within the string