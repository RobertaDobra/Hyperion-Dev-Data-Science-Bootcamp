sentence=str(input("Enter a sentence: "))
x=sentence.split()
for word in x:
    print(word)
    
#I tried the following code but I did not understand why the words are not printed on a new line: print(sentence.split("/n"))