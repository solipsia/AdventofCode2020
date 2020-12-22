rawdata = open("16-1.input.txt").readlines()

mode=1
your=[]
nearby=[]
valid=[]
for line in rawdata:
    if "your ticket:" in line:
        mode=2
        continue
    if "nearby tickets:" in line:
        mode=3
        continue
    if mode==1 and len(line)>2:
        valid+=range(int(line.split("-")[0].split(" ")[-1]),int(line.split("-")[1].split(" ")[0])+1)
        valid+=range(int(line.split("-")[1].split(" ")[2]),int(line.split("-")[2])+1)
    if mode==2 and len(line)>2:
        your=[int(i) for i in line.strip().split(",")]
    if mode==3 and len(line)>2:
        nearby.append([int(i) for i in line.strip().split(",")])

err=0
for ticket in nearby:
    for field in ticket:
        if field not in valid:
            err=err+field

print(err)
