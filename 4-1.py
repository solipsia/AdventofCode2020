
import re
import copy
rawdata = open("4-1.input.txt").read()
passports = []
for item in re.split("\n\n",rawdata):
    passports.append((item))

requiredfields = ['byr','iyr','eyr','hgt','hcl', 'ecl','pid']

valids = 0
for passport in passports:
    currentfields=copy.deepcopy(requiredfields)
    valid=1
    for field in re.split('\n| ',passport):
        if field.split(':')[0] in currentfields:
            currentfields.remove(field.split(':')[0])
    if len(currentfields)>0:
        valid=0
    valids=valids+valid

print(valids)