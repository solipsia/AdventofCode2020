
rawdata = open("7-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append((item))

rules={}

for rule in data:
    outerbag=rule.split(' bags contain ')[0]
    contents=rule.split(' bags contain ')[1].split(', ')
    for innerbag in contents:
        innerbag=innerbag.replace(' bags','').replace('.','').replace('\n','').replace(' bag','')
        if innerbag!='no other':
            num=int(innerbag[0])
            innerbag=innerbag[2:]
        else:
            num=0
            innerbag=''
        if outerbag in rules:
            rules[outerbag]=rules[outerbag]+[innerbag]*num
        else:
            rules[outerbag]=[innerbag]*num

def numinnerbags(outerbag):
    if rules[outerbag]==[]:
        return 0
    else:
        total=0
        for innerbag in rules[outerbag]:
            total=total+1+numinnerbags(innerbag)
        return total

print(numinnerbags("shiny gold"))