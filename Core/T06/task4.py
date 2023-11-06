x=int(input("Input an integer:"))
if x % 2 == 0 and x % 5 == 0:
    print("Your number is divisible by 2 and 5")
elif x % 2 == 0 or x % 5 == 0:
    print("Your number is divisible by 2 or 5")
elif x % 2 != 0 or x % 5 != 0:
    print("Your number is not divisible by 2 or 5")