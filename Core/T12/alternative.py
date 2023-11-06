string = "Hello World"
res = ""
for index in range(len(string)):
    if index %2==0:
        res = res + string[index].upper()
    else:
        res = res + string[index].lower()
print(res)

string="I am learning to code"
x=string.split()
res = ""

for i in range(len(x)):
    if i%2!=0:
        res=res+ " " + x[i].lower()
    else:
        res=res+ " " + x[i].upper()
    
print(res)