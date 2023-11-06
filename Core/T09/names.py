count=0    
x=str(input("Enter the names of all pupils. Type 'Stop' after entering all names: "))   
while True:
    x = input("Enter a name: ")
    count=count+1 
    if x == "Stop":
        print(count)
        break 