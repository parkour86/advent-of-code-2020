with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

cnt = 0
newInput = []
for line in input:
    if line != '':
        newInput.append(line)
    else:
        flag = True
        if len(newInput) > 1:
            intercept = newInput[0]
            for i in range(len(newInput)):
                for j in range(1+i,len(newInput)):
                    intercept = set(intercept).intersection(newInput[j])
                    if intercept and flag:
                        flag = True
                    else:
                        flag = False
            if flag:
                cnt += len(intercept)
        else:
            cnt += len(newInput[0])
        newInput.clear()

print(cnt)
