
rawdata = open("5-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append((item))
   
highest=0
for bp in data:
    pos=7
    row=0
    col=0
    rowstr=bp[:7]
    for c in rowstr:
        if c=='B':
            row=row+pow(2,pos-1)
        pos=pos-1
    colstr=bp[7:10]    
    pos=3
    for c in colstr:
        if c=='R':
            col=col+pow(2,pos-1)
        pos=pos-1
    id=row*8+col
    highest =max([highest,id])
print(highest)
