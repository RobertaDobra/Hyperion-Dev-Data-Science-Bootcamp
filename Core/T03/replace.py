sentence= " T h e ! q u i c k ! b r o w n ! f o x ! j u m p s ! o v e r ! t h e ! l a z y ! d o g ! . "
sentence=sentence.replace(" ", "")
sentence=sentence.replace("!", " ")
print(sentence)
sentence=sentence.upper()
print(sentence)
print(sentence[::-1])