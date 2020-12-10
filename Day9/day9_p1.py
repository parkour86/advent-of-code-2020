with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

preamble = 55

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
        print(num)
        return False

# loop over the input file stepping on the 5th item
for number in range(preamble,len(input)):
    decipher(number,input[number])
