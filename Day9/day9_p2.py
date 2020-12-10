with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

preamble = 25

def decipher(index,num):
    # loop over the last 5
    for i in range(index-preamble,index-1):
        for j in range(index-preamble,index):
            # Make sure it doesn't sum it's own number
            if i != j:
                sum = int(input[i])+int(input[j])
                if sum == int(num):
                    return True
    else:
        return num

def contiguous(num):
    if type(num) == str:
        for i in range(len(input)):
            total = int(num)
            for j in range(i,len(input)):
                total -= int(input[j])
                if total < 0:
                    total = int(num)
                    break
                elif total == 0:
                    # Found the number range that add up to the decipher
                    list = [input[k] for k in range(i,j+1)]
                    print(int(max(list))+int(min(list)))
                    return True

# loop over the input file stepping on the 5th item
for number in range(preamble,len(input)):
    contiguous(decipher(number,input[number]))
