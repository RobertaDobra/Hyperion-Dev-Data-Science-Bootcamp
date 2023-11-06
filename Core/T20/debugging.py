def print_values_of(dictionary, keys):
    for k in keys:
        print(dictionary[k]) #k was undefined

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh!", "maggie": "(Pacifier Suck)"} #unterminated string literal for value of key homer

#print_values_of() takes 2 positional arguments i.e dict and keys but 4 were given in the file meant for debugging, keys had more than one argument so I converted the 3 keys into a list as input for keys argument
print_values_of(simpson_catch_phrases, ["lisa", "bart", "homer"])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

