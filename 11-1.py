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
    return int(seats[y-1][x]=='#')+int(seats[y-1][x+1]=='#')+int(seats[y][x+1]=='#')+int(seats[y+1][x+1]=='#')+int(seats[y+1][x]=='#')+int(seats[y+1][x-1]=='#')+int(seats[y][x-1]=='#')+int(seats[y-1][x-1]=='#')

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
#showseats()
while changes==1:
    changes=0
    for y in range(1,maxy-1):
        for x in range(1,maxx-1):
            if seats[y][x]=='L' and occupied(x,y)==0:
                next[y][x]='#'
                changes=1
            if seats[y][x]=='#' and occupied(x,y)>=4:
                next[y][x]='L'
                changes=1
        
    flip()
    #showseats()

totalocc=0
for y in range(maxy):
        for x in range(maxx):
            if seats[y][x]=='#':
                totalocc=totalocc+1
print(totalocc)