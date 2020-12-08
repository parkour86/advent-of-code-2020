with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

def modifyAll(bagObject,keyValue):
    for key in bagObject.keys():
        for index,bags in enumerate(bagObject[key]):
            if keyValue == bags:
                bagObject[key][index] = "shiny gold"

# Clean up the input file
bagObject = {}
for line in input:
    # Remove digits and bag/bags keywords
    list = ''.join([i for i in line if not i.isdigit()]).replace('bags','').replace('bag','').replace('.','')
    bagList = list.split('contain')[0].strip()
    # Create a list of bag items
    bagItems = list.split('contain')[1].split(',')
    bagObject[bagList] = [value.strip() for value in bagItems]

# Loop over the keys and check if they contain shiny gold
for _ in range(10):
    for key in bagObject.keys():
        if "shiny gold" in bagObject[key]:
            modifyAll(bagObject,key)

# Count the number of times shiny gold exists in a key
cnt = 0
for key in bagObject.keys():
    if "shiny gold" in bagObject[key]:
        print(key,'=',bagObject[key])
        cnt += 1

print('')
print(cnt)
