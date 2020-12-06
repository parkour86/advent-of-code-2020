with open('input.txt', 'r+') as file:
    input = file.readlines()

cnt = 0
for i in input:
    line = i.replace(':','').split(' ')
    print(line)
    pos1 = int(line[0].split('-')[0])
    pos2 = int(line[0].split('-')[1])
    letter = line[1]
    occurence = line[2].count(letter)

    if occurence >= pos1 and occurence <= pos2:
        cnt += 1
print(cnt)
