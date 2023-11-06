mines = [ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]

#neighbour diagonally, horizontally or vertically, use value at certain index for row and col, max 6 possibe neighbours bearing in mind we can't go beyond the margins
#if row=o, row-1 runs error
#if row=4, row+1 runs error
#if col=0, col-1 runs erros
#if col=4, col+1 runs eror
for row in range(len(mines)):
    for col in range(len(mines)):
        counter=0
        if mines[row][col] == "-": #needs to count all #, if it wasn't specified it should equal "-", it might equal "#"" and would count neighbours but not itself
            if row>0:
                if col>0 and mines[row-1][col-1] == "#":
                    counter=counter+1
                if mines[row-1][col] == "#":
                    counter=counter+1
                if col < 4 and mines[row-1][col+1] == "#":
                    counter=counter+1
            if col>0 and mines[row][col-1] == "#":
                counter=counter+1
            if col < 4 and mines[row][col+1] == "#":
                counter=counter+1
            if row<4:
                if col>0 and mines[row+1][col-1] == "#":
                    counter=counter+1
                if mines[row+1][col] == "#":
                    counter=counter+1
                if col < 4 and mines[row+1][col+1] == "#":
                    counter=counter+1
            mines[row][col]=str(counter)
print(mines)