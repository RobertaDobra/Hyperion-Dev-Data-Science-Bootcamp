students = int(input("Please enter the number of students in class: "))
id_number = ""
for i in range(0, students):
    id_number=int(input("Enter your id: "))
with open('reg_form.txt', 'w') as file:
    for id_number in range(1, students+1):
        file.write("Student ID numbers: \n" + "........." + str(id_number) + "\n")
