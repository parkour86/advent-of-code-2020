with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

flag = 0
seats = []
currOccupied = 0
prevOccupied = 9
while prevOccupied != currOccupied:
    prevOccupied = currOccupied
    currOccupied = 0
    prev = ''
    # Grab the whole row
    for i,line in enumerate(input):
        newLine = ''
        # Loop over the seats
        for j in range(len(line)):
            cnt = 0
            if line[j] == 'L':
                start = 0 if j-1 < 0 else j-1
                end = len(line) if j+2 > len(line) else j+2
                if prev:
                    top = all(prev[k] == 'L' or prev[k] == '.' for k in range(start,end))
                else:
                    top = True
                left = (line[j-1] == 'L' or line[j-1] == '.') if j-1 >= 0 else True
                right = (line[j+1] == 'L' or line[j+1] == '.') if j+1 != len(line) else True
                if i+1 < len(input):
                    bottom = all(input[i+1][k] == 'L' or input[i+1][k] == '.' for k in range(start,end))
                else:
                    bottom = True
                if (top and left and right and bottom and True):
                    newLine += '#'
                    currOccupied += 1
                else:
                    newLine += 'L'
            elif line[j] == '.':
                newLine += '.'
            elif line[j] == '#':
                start = 0 if j-1 < 0 else j-1
                end = len(line) if j+2 > len(line) else j+2
                # Check the top
                if prev:
                    for k in range(start,end):
                        if prev[k] == '#':
                            cnt += 1
                # Check the left
                if j-1 >= 0 and line[j-1] == '#':
                        cnt += 1
                # Check the right
                if j+1 != len(line) and line[j+1] == '#':
                    cnt += 1
                # Check the bottom
                if i+1 < len(input):
                    for k in range(start,end):
                        if input[i+1][k] == '#':
                            cnt += 1
                # Check if there's 4 occupied seats
                if cnt >= 4:
                    newLine += 'L'
                else:
                    newLine += '#'
                    currOccupied += 1
        seats.append(newLine)
        prev = line
    input.clear()
    for i in range(len(seats)):
        #print(seats[i])
        input.append(seats[i])
    seats.clear()

print('Occupied',currOccupied)
