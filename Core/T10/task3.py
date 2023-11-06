#while loop of countdown from 20 to 0:
i=20
while i >=0:
    print(i)
    i=i-1

#all even number between 1 and 20 using:
i=1
while i<20:
    if i%2==0:
        print(i)
    i=i+1

#***** output:
i="*"
while i<=5*"*":
    print(i)
    i=i+ "*"

#hcf
x=int(input("Input a positive number: "))
y=int(input("Input a positive number: "))
i=1
while i<=x and i<=y:
    if x%i==0 and y%i==0:
        print(i)
    i=i+1
print("Highest common factor is the last value from the iteration")        
    