def minimum(nums):
    return min(nums)

def maximum(nums):
    return max(nums)

def avg(nums):
    return sum(nums)/len(nums)

f=open("input.txt", "r") #open file
lines=f.readlines() #reads each line on a separate line
lines[0]=lines[0].strip('\n').strip("ï»¿").split(":") #lines[0] is first line from input.txt i.e min:1,2..., I stripped the odd character in front of min, stripped the newline character and split by the : delimiter from the original text
nums_list=lines[0][1].split(",") #retrieve second element from list and split by the , delimiter from original text to get list of the individual numbers split by a comma 
lines[1]=lines[1].strip('\n').split(":")
lines[2]=lines[2].strip('\n').split(":")

for i in range(len(nums_list)): #convert from string to int
    nums_list[i]=int(nums_list[i])

out=open("output.txt", "a")
if lines[0][0] == "min": #retrieve first element from list
    out.write(f"The min of {nums_list} is {minimum(nums_list)}\n") #write to file
if lines[1][0] == "max":
    out.write(f"The max of {nums_list} is {maximum(nums_list)}\n")
if lines[2][0] == "avg":
    out.write(f"The avg of {nums_list} is {avg(nums_list)}\n") 
     