name=str(input("input your full name: "))
x=name.split() #separates each word in given string
#len(name) counts number of characters in the string
#len(x) counts number of words in the string
if len(name) == 0:
    print("You haven't entered anything. Please enter your full name")
elif len(name) >= 2 and len(name) <=25 and len(x) >= 2 and len(name) >= 4 and len(name) <= 25:
    print("Thank you for entering your name")
elif len(x) < 2:
    print("Please enter your name and surname")
elif len(name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name")