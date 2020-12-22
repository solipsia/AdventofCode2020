import copy
rawdata = open("16-1.input.txt").readlines()

mode=1
your=[]
nearby=[]
valid=[]
fields=[]
fieldcount=0
for line in rawdata:
    if "your ticket:" in line:
        mode=2
        continue
    if "nearby tickets:" in line:
        mode=3
        continue
    if mode==1 and len(line)>2:
        limits=[]
        limits.append(fieldcount)
        limits.append(int(line.split("-")[0].split(" ")[-1]))
        limits.append(int(line.split("-")[1].split(" ")[0]))
        limits.append(int(line.split("-")[1].split(" ")[2]))
        limits.append(int(line.split("-")[2]))
        fields.append(limits)
        valid+=range(int(line.split("-")[0].split(" ")[-1]),int(line.split("-")[1].split(" ")[0])+1)
        valid+=range(int(line.split("-")[1].split(" ")[2]),int(line.split("-")[2])+1)
        fieldcount+=1
    if mode==2 and len(line)>2:
        your=[int(i) for i in line.strip().split(",")]
    if mode==3 and len(line)>2:
        nearby.append([int(i) for i in line.strip().split(",")])

err=0
validtickets=copy.deepcopy(nearby)
for ticket in nearby:
    for field in ticket:
        if field not in valid:
            validtickets.remove(ticket)
            break

col=[]
for i in range(len(nearby[0])):
    col.append(list(range(fieldcount)))

for tries in range(10):
    for ticket in validtickets:
        for colnum,val in enumerate(ticket):
            for fieldnum,fieldmin1,fieldmax1,fieldmin2,fieldmax2 in fields:
                if val not in range(fieldmin1,fieldmax1+1) and val not in range(fieldmin2,fieldmax2+1):
                    if fieldnum in col[colnum]:
                        col[colnum].remove(fieldnum)
                    if len(col[colnum])==1:
                        for i in range(len(col)):
                            if i!=colnum and col[colnum][0] in col[i]:
                                col[i].remove(col[colnum][0])
                #

fieldmappings=[]
for c in col:
    fieldmappings.append(c[0])

ans=1
for colindex,colvalue in enumerate(your):
    if fieldmappings[colindex]<=5:
        ans*=colvalue

print(ans)