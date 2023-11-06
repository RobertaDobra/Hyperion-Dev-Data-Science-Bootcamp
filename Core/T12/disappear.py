sentence=str(input("Enter a sentence: "))
char=str(input("Enter characters you would want removed from the sentence: "))
for char in char:
    sentence= sentence.replace(char, "")
print(sentence)