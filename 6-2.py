

import re
import copy
rawdata = open("6-1.input.txt").read()
groups = []
for item in re.split("\n\n",rawdata):
    groups.append((item))

sum=0
for group in groups:
    answers={}
    for person in group.split('\n'):
        for answer in person:
            if answer not in answers:
                answers[answer]=1
            else:
                answers[answer]=answers[answer]+1
    for a in answers:
        if answers[a]==len(group.split('\n')):
            sum=sum+1
print(sum)