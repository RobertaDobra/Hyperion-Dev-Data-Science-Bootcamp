animal = "Lion" #name error: 'Lion' is not defined
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a " + str(animal) +". It is a " + str(animal_type) + " and it has " + str(number_of_teeth) + " teeth " #TypeError: can only concatenate str (not "int") to str; logic error so I re-worded the phrase

print(full_spec) #syntax error: missing parentheses