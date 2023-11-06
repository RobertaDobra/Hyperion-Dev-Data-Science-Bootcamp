print("Welcome to the error program") #syntax error, missing parentheses
print("\n") #syntax error, missing parentheses

ageStr = "24" #I'm 24 years old. #syntax error: indentation; runtime name error: ageStr not defined
age = int(ageStr) #syntax error: indentation; value error: invalid literal for int() so I deleted years old from ageStr so python could convert 24 string into an integer
print("I'm "+ str(age) + " years old.") #syntax error: indentation; type error: I converted age into string because python cannot concatenate str and int values
three = "3" #syntax error, indentation

answerYears = age + int(three) #syntax error, indentation; type error because python cannot add int and str so I converted three into int

print("The total number of years:" + str(answerYears)) #syntax error, missing parentheses; type error: I converted answerYears into str from int because python cannot concatenate str and int values
answerMonths = answerYears * 12 + 6 # runtime error name error: name 'answer' not defined so I switched answer with answerYears; logic error: programme runs but does not correctly answer the question so I added 6 months because the answer needs to be calculated after 3 years(answerYears was already inputted correctly) and 6 months
print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old") #syntax error, missing parentheses; type error because python cannot add int and str so I converted answerMonths into str  

#HINT, 330 months is the correct answer