import math

with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

row = 127
column = 7
highest = 0
boardingPass = []
for list in range(len(input)):
    rowStart = 0
    rowEnd = 127
    columnStart = 0
    columnEnd = 7
    # Find the row
    for rowLetter in input[list][:7]:
        if rowLetter == 'F':
            rowEnd = rowStart + (rowEnd - rowStart) // 2
        if rowLetter == 'B':
            rowStart = rowStart + math.ceil((rowEnd - rowStart)/2)
        if rowStart == rowEnd:
            row = rowStart
            break
    # Find the column
    for columnLetter in input[list][7:]:
        if columnLetter == 'L':
            columnEnd = columnStart + (columnEnd - columnStart) // 2
        if columnLetter == 'R':
            columnStart = columnStart + math.ceil((columnEnd - columnStart)/2)
        if columnStart == columnEnd:
            column = columnStart
            break
    passID = row*8+column
    boardingPass.append(passID)
    if passID > highest:
        highest = passID
#print(highest)


boardingPass.sort()
for x in boardingPass:
    if int(x)+1 not in boardingPass and int(x)+1 < highest:
        print(int(x)+1)
