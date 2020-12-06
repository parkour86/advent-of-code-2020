with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

cnt = 0
newInput = set()
for line in input:
    if line != '':
        for letter in line:
            newInput.add(letter)
    else:
        cnt += len(newInput)
        newInput.clear()
print(cnt)
