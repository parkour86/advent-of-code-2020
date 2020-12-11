with open('input.txt', 'r+') as file:
    input = file.readlines()

diff1 = 0
diff5 = 0
jolt = 0

input = [int(x) for x in input]
input.sort()
input.append(max(input)+3)

for i,v in enumerate(input):
    if jolt+1 == v:
        jolt += 1
        diff1 += 1
    elif jolt+3 == v:
        jolt += 3
        diff5 += 1

print(diff1,diff5)
print(diff1*diff5)
