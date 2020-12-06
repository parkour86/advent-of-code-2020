with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

def slope(R,D):
    index = 0
    cnt = 0
    for line in range(0,len(input),D):
        if input[line]:
            if index > 30:
                index -= 31
            if input[line][index] == '#':
                cnt += 1
            # This area is for displaying the input
            # temp = ''
            # for inx,i in enumerate(input[line]):
            #     if inx == index:
            #         if i == '#':
            #             cnt += 1
            #             temp += '\033[32mO'
            #         else:
            #             temp += '\033[36mO'
            #     else:
            #         temp += '\033[37m'+i
            #print(temp,input[line],index)
            index += R
    return cnt


print(slope(1,1))
print(slope(3,1))
print(slope(5,1))
print(slope(7,1))
print(slope(1,2))
