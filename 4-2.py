
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
        type=field.split(':')[0]
        val=field.split(':')[1]
        if type in currentfields:
            currentfields.remove(type)
        if (type=='byr' and (int(val)<1920 or int(val)>2002)) or \
           (type=='iyr' and (int(val)<2010 or int(val)>2020)) or \
           (type=='eyr' and (int(val)<2020 or int(val)>2030)): 
            valid=0
        if type=='hgt':
            if val[-2:] not in ['cm','in']:
                valid=0
            if val[-2:]=='cm' and (int(val[:-2])<150 or int(val[:-2])>193):
                valid=0
            if val[-2:]=='in' and (int(val[:-2])<59 or int(val[:-2])>76):
                valid=0 
        if (type=='hcl' and not re.match("#[0-9a-fA-F]{6}",val)):
            valid=0
        if (type=='ecl' and val not in ['amb','blu','brn','gry','grn','hzl','oth']):
            valid=0
        if (type=='pid' and not re.match("^\\d{9}$",val)):
            valid=0
    if len(currentfields)>0:
        valid=0
    valids=valids+valid

print(valids)