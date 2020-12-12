

import re
import copy
rawdata = open("6-1.input.txt").read()
groups = []
for item in re.split("\n\n",rawdata):
    groups.append((item))

sum=0
for group in groups:
    answers=[]
    for person in group.split('\n'):
        for answer in person:
            if answer not in answers:
                answers.append(answer)
    sum=sum+len(answers)
print(sum)