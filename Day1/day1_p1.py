with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

def loop(num,input):
    for i in range(len(input)-1):
        print(num,input[i])
        if int(input[i])+num == 2020:
            return int(input[i])*num

for i in range(len(input)):
    output = loop(int(input[i]),input)
    if output:
        print(output)
        break
