days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def my_function():
  print(days)
my_function() #function is called, prints days which is a list


def replace_strr():
    string=str(input("Enter a sentence: "))
    x=string.split() #breaks up the string so individual words can be processed
    res= ""
    for i in range(len(x)): #length of list, i.e number of words in the list
        if i%2==0: #if index is an even number 
            res=res+ " " + x[i] #word at i index stays the same
        else: #if index is odd
            res=res+ " " + "Hello" #each second word is replaced with 'Hello', indexing starts at 0, word at index 1 is replaced with Hello, word[2] stays the same and so on
    print(res)
replace_strr() #function is called, replaces each second word of given input sentence from user