with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

def non():
    for i in range(len(input)):
        for k in range(len(input)-1):
            for j in range(len(input)-1):
                if input[i].isdigit() and input[k].isdigit():
                    first = int(input[i])
                    second = int(input[k])
                    third = int(input[j])
                    print(input[i],input[k],input[j], end=' ')
                    print(first+second+third)
                    if first+second+third == 2020:
                        print(first*second*third)
                        return 0
non()
