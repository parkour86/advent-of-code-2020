with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

earliestDepart = int(input[0])
busID = [x for x in input[1].split(',') if x != 'x']

for i in range(0,earliestDepart+1000):
    for j in range(len(busID)):
        if i % int(busID[j]) == 0 and i >= earliestDepart:
            print('Time:',i,'\nBus ID:',busID[j])
            calc = (i-earliestDepart)*int(busID[j])
            print('Answer',calc)
            break
    else:
        continue
    break
