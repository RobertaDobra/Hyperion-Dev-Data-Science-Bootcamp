numbers1=[1,3,5,7,9]
numbers2=[2,4,6,8,10]
all_numbers = numbers1 + numbers2
all_numbers = sorted(all_numbers)
print(all_numbers) 


with open("numbers1.txt", "w") as file:
    file.write(str(numbers1))
with open("numbers2.txt", "w") as file:
    file.write(str(numbers2))

with open("all_numbers.txt", "w") as file:
    file.write(str(all_numbers))