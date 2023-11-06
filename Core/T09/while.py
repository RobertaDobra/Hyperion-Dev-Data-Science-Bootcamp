count=0
total=0
i=int(input("Enter a number: "))
while i!=-1:
    count=count+1
    total=total+i
    i=int(input("Enter a number: "))
print(total/count)