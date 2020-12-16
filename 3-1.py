
rawdata = open("3-1.input.txt").readlines()
treehits=0
x=0
for line in rawdata:
    if line[x%(len(line)-1)]=='#':
        treehits=treehits+1
    x=x+3
print(treehits) 