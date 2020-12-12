import copy
rawdata = open("11-1.input.txt").readlines()
seats = list(["x"*(2+len(rawdata[0].replace('\n','')))])
for item in rawdata:
    seats.append(list('x'+item.replace('\n','')+'x') )
seats.append(list("x"*(2+len(rawdata[0].replace('\n',''))))) 

changes=0
maxx=len(seats[0])
maxy=len(seats)

next=[['.']*len(seats[0])]*len(seats)

for y in range(maxy):
    for x in range(maxx):
        next[y]=copy.deepcopy(seats[y])

def occupied(x,y):
    tally=0
    x1=x
    y1=y
    #up
    while (x1==x and y1==y) or seats[y1][x1] not in ['x','L']:
        if not (x1==x and y1==y) and seats[y1][x1]=='#':
            tally=tally+1
            break
        y1=y1-1
    #up right
    x1=x
    y1=y
    while (x1==x and y1==y) or seats[y1][x1] not in ['x','L']:
        if not (x1==x and y1==y) and seats[y1][x1]=='#':
            tally=tally+1
            break
        y1=y1-1
        x1=x1+1
    #right
    x1=x
    y1=y
    while (x1==x and y1==y) or seats[y1][x1] not in ['x','L']:
        if not (x1==x and y1==y) and seats[y1][x1]=='#':
            tally=tally+1
            break
        x1=x1+1
    #down right
    x1=x
    y1=y
    while (x1==x and y1==y) or seats[y1][x1] not in ['x','L']:
        if not (x1==x and y1==y) and seats[y1][x1]=='#':
            tally=tally+1
            break
        y1=y1+1
        x1=x1+1
    #down
    x1=x
    y1=y
    while (x1==x and y1==y) or seats[y1][x1] not in ['x','L']:
        if not (x1==x and y1==y) and seats[y1][x1]=='#':
            tally=tally+1
            break
        y1=y1+1
    #down left
    x1=x
    y1=y
    while (x1==x and y1==y) or seats[y1][x1] not in ['x','L']:
        if not (x1==x and y1==y) and seats[y1][x1]=='#':
            tally=tally+1
            break
        y1=y1+1
        x1=x1-1
    #left
    x1=x
    y1=y
    while (x1==x and y1==y) or seats[y1][x1] not in ['x','L']:
        if not (x1==x and y1==y) and seats[y1][x1]=='#':
            tally=tally+1
            break
        x1=x1-1
    #up left
    x1=x
    y1=y
    while (x1==x and y1==y) or seats[y1][x1] not in ['x','L']:
        if not (x1==x and y1==y) and seats[y1][x1]=='#':
            tally=tally+1
            break
        y1=y1-1
        x1=x1-1
    return tally

def showseats():
    for y in range(maxy):
        row=''
        for x in range(maxx):
            row=row+seats[y][x]
        print(row)

def flip():
    for y in range(maxy):
        for x in range(maxx):
            seats[y]=copy.deepcopy(next[y])

changes=1
showseats()


while changes==1:
    changes=0
    for y in range(1,maxy-1):
        for x in range(1,maxx-1):
            if seats[y][x]=='L' and occupied(x,y)==0:
                next[y][x]='#'
                changes=1
            if seats[y][x]=='#' and occupied(x,y)>=5:
                next[y][x]='L'
                changes=1
        
    flip()

totalocc=0
for y in range(maxy):
        for x in range(maxx):
            if seats[y][x]=='#':
                totalocc=totalocc+1
print(totalocc)