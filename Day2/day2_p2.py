
with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

cnt = 0
for i in input:
    line = i.replace(':','').split(' ')
    pos1 = int(line[0].split('-')[0])-1
    pos2 = int(line[0].split('-')[1])-1
    letter = line[1]
    occurence = line[2].count(letter)
    bool1 = line[2][pos1:pos1+1] == letter
    bool2 = line[2][pos2:pos2+1] == letter

    if bool1 != bool2:
        cnt += 1
print(cnt)
