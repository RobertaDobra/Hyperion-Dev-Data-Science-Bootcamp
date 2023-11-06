x=str(input("Enter a word: "))
if x == x[::-1]:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")