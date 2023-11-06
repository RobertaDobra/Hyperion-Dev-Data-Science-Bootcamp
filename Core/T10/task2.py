y=int(input("Enter a year: "))
n=int(input("Enter a number of years: "))
for x in range(1, n+1):
    if (y+x)%4==0:
        print(str(y+x) + " is a leap year")
    if (y+x)%4!=0:
        print(y+x)