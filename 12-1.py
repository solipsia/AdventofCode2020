rawdata = open("12-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append(item.replace('\n',''))

dirs=['E','S','W','N']
dirsx=[1,0,-1,0]
dirsy=[0,1,0,-1]
dir=0
x=0
y=0
print(dirs[dir],x,y)
for ins in data:
    act=ins[:1]
    val=int(ins[1:])
    if act=='R':
        dir=(dir+int(val/90))%4
    if act=='L':
        dir=(dir-int(val/90))%4
    if act=='N':
        y=y-val
    if act=='S':
        y=y+val
    if act=='E':
        x=x+val
    if act=='W':
        x=x-val
    if act=='F':
        x=x+dirsx[dir]*val
        y=y+dirsy[dir]*val
print(abs(x)+abs(y))