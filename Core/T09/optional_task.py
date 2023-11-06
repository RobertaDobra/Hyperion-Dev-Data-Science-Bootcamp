i=int(input("Enter a number less than or equal to 100: "))
if i>100:
     print("Try again")
     i=int(input("Enter a number less than or equal to 100: "))
while i<=100:
    if i%2==0:
        print(i*2)
        break
    elif i%2!=0:
        print(i*3)
        break