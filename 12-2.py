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
wpx=10
wpy=-1
print(dirs[dir],x,y)
for ins in data:
    act=ins[:1]
    val=int(ins[1:])
    if act=='R':
        if (int(val/90))%4==1:
            oldx=wpx
            oldy=wpy
            wpy=oldx
            wpx=-oldy
        if (int(val/90))%4==2:
            wpx=-wpx
            wpy=-wpy
        if (int(val/90))%4==3:
            oldx=wpx
            oldy=wpy
            wpy=-oldx
            wpx=oldy
    if act=='L':
        if (int(val/90))%4==3:
            oldx=wpx
            oldy=wpy
            wpy=oldx
            wpx=-oldy
        if (int(val/90))%4==2:
            wpx=-wpx
            wpy=-wpy
        if (int(val/90))%4==1:
            oldx=wpx
            oldy=wpy
            wpy=-oldx
            wpx=oldy
    if act=='N':
        wpy=wpy-val
    if act=='S':
        wpy=wpy+val
    if act=='E':
        wpx=wpx+val
    if act=='W':
        wpx=wpx-val
    if act=='F':
        x=x+wpx*val
        y=y+wpy*val

print(abs(x)+abs(y))
