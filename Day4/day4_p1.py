import re

with open('input.txt', 'r+') as file:
    input = file.read().split('\n')

valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

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
    if all(x+':' in i for x in valid):
        cnt += 1

print(cnt)
