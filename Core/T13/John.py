name = input("Please enter a name, enter John to end the task: ")
name_list = []
while name != "John":
    name_list.append(name)
    name = input("Please enter a name: ")
print(name_list)
