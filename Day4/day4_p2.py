import re

with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.

def validate(field,data):
    if field == 'byr' and len(data) == 4 and int(data) >= 1920 and int(data) <= 2002:
        return True
    if field == 'iyr' and len(data) == 4 and int(data) >= 2010 and int(data) <= 2020:
        return True
    if field == 'eyr' and len(data) == 4 and int(data) >= 2020 and int(data) <= 2030:
        return True
    if field == 'hgt' and ('cm' in data and int(data.replace('cm','')) >= 150 and int(data.replace('cm','')) <= 193 or 'in' in data and int(data.replace('in','')) >= 59 and int(data.replace('in','')) <= 76):
        return True
    if field == 'hcl' and re.search("^#[0-9 a-f]{6}$", data):
        return True
    valid = ['amb','blu','brn','gry','grn','hzl','oth']
    if field == 'ecl' and any(x in data for x in valid):
        return True
    if field == 'pid' and len(data) == 9:
        return True
    if field == 'cid':
        return True
    return False

cnt = 0
newInput = []
temp = ''
# Place all passport data into one string and store in a list
for i in input:
    if i != '':
        temp += i + ' '
    else:
        newInput.append(temp.strip())
        print(temp)
        temp = ''

print('------------')
# Loop over each passport data
for i in newInput:
    flag = True
    if all(x+':' in i for x in valid):
        print(' ')
        print(i)
        splitLine = i.split(' ')
        for j in splitLine:
            print(j)
            print(validate(j.split(':')[0],j.split(':')[1]))
            if not validate(j.split(':')[0],j.split(':')[1]):
                flag = False
                break
        if flag:
            cnt += 1

print(cnt)
